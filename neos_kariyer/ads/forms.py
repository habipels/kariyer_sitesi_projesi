from django import forms
from .models import *
class is_ilan(forms.ModelForm):
    class Meta:
        model = ads_data
        fields = ["ilan_basligi","kisa_ilan_aciklamasi","ilan","İlan_gorseli"]
