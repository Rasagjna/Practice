from socket import fromshare
from django import forms
class ProfileForm(forms.Form):
    # user_image = forms.FileField()
    user_image = forms.ImageField()
    #ImageFIeld also can be used for image specific
