from rest_framework import serializers
from .models import *
class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields='__all__'
class eventTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventTypes
        fields='__all__'
        depth=1

class WorkshopsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Workshops
        fields='__all__'
        depth=2
class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sports
        fields='__all__'
        depth=2
class EmployeeWellnessSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeWellness
        fields='__all__'
        depth=2  
class DonationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donations
        fields='__all__'
        depth=1  
        
        
class UserDonationsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDonation
        fields='__all__'
        depth=1  
class MyfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExampleFiles
        fields="__all__"
class HackathonSerializer(serializers.ModelSerializer):

    class Meta:

        model=Hackathon

        fields='__all__'
class ArtsSerializer(serializers.ModelSerializer):

    class Meta:

        model=Arts

        fields='__all__'

        depth=1
class TimeLinesSerializer(serializers.ModelSerializer):

    class Meta:

        model=TimeLines

        fields='__all__'

        depth=1
class OrganizersSerializer(serializers.ModelSerializer):
    class Meta:

        model=Organizers

        fields='__all__'

        depth=1
class MyfileSerializer(serializers.ModelSerializer):
    class Meta:

        model=ExampleFiles

        fields='__all__'

        depth=1
class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance