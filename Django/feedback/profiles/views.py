from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView
from rest_framework.permissions import IsAuthenticated
from .forms import ProfileForm
from .models import UserProfile

# Create your views here.
# def store_file(file):
#     with open("temp/html.txt","wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(CreateView):
    model=UserProfile
    fields = "__all__"
    template_name = "profiles/create_profile.html"
    success_url = "/profiles"
# class CreateProfileView(View):
#     def get(self, request):
#         form=ProfileForm()
#         return render(request, "profiles/create_profile.html",{
#             "form":form
#         })

#     def post(self, request):
#         # print(request.FILES["image"])
#         submited_form = ProfileForm(request.POST,request.FILES)
#         if submited_form.is_valid():

#             # store_file(request.FILES["image"])
#             profile= UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
#         return render(request,"profiles/create_profile.html",{
#             "form":submited_form
#         })
        
# class ProfilesView(ListView):
#     model=UserProfile
#     template_name = "profiles/user_profiles.html"
#     context_object_name = "profiles"
from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


# @csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
    
@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)