from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    # path("list",views.ProfilesView.as_view()),
    path("login/",views.login),
    path("sampleapi/",views.sample_api)]