class EmployeeCRUDSerializer(serializers.ModelSerializer):
    role = serializers.SlugRelatedField(queryset=Role.objects.all(),slug_field = "role_name")
    department = serializers.SlugRelatedField(queryset=Department.objects.all(),slug_field = "department_name")
    sub_department = serializers.SlugRelatedField(queryset=SubDepartment.objects.all(),slug_field = "sub_department_name")
    manager = serializers.SlugRelatedField(queryset=Employee.objects.all(),allow_null=True,slug_field = "employee_code")
    dotted_line_manager = serializers.SlugRelatedField(queryset=Employee.objects.all(),slug_field = "employee_code",allow_null=True)
    manager_name = serializers.CharField(source='manager.display_name', read_only=True)
    dotted_line_manager_name = serializers.CharField(source='dotted_line_manager.display_name',read_only=True)
    class Meta:
        model = Employee
        exclude = ["user_permissions","is_superuser","last_login","password"]
    
    def to_representation(self, instance):
        for_dropdown:bool = self.context.get("for_dropdown")
        representation = super().to_representation(instance)
        representation["groups"] ={Group.objects.filter(id = group_id).first().name: group_id for group_id in representation["groups"]}
        
        if for_dropdown == "true":
            data = {representation["display_name"]: representation["employee_code"]}
            return data
        return representation
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = Employee.USERNAME_FIELD
    def validate(self, attrs):

        # The default result (access/refresh tokens)

        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'email': self.user.email})
        data.update({'employee_code':self.user.employee_code})
        return data
    
#####----------------------  views -------------------############
class CustomTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def generate_logical_password(self,username:str):
        password = f"{username}_{str(settings.SECRET_KEY)}"
        return password

    def get(self, request, *args, **kwargs):
        base_url="https://graph.microsoft.com/v1.0/"
        endpoint=base_url + 'me'
        access_token_id= request.META.get('HTTP_AUTHORIZATION')
        headers={'Authorization':access_token_id}
        response=requests.get(endpoint,headers=headers)
        data=response.json()
        print(data,"------")
        email = data['mail']
        request.data['email']=str(email).lower()
        request.data['password'] = self.generate_logical_password(username = email)
        user = get_user_model().objects.filter(email = email)
        if user.exists() and not user.first().password:
            print("inside")
            serializer = EmployeeSerializer(user.first(),data = {"password":self.generate_logical_password(username=email)},partial = True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        try:
            response = super().post(request, *args, **kwargs)
            return response
        except Exception as e:
            traceback.print_exc()
            return Response(
                {"error": str(e)},
                status=500
            )