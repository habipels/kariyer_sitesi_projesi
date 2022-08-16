from django import forms
from .models import user_profil ,company_profile

class user_back_img(forms.ModelForm):
    class Meta:
        model = user_profil
        fields = ["background"]

class user_profile_img(forms.ModelForm):
    class Meta:
        model = user_profil
        fields = ["profil_img"]

class long_dec(forms.ModelForm):
    class Meta:
        model = company_profile
        fields = ["company_about"]