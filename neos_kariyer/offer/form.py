from django import forms
from .models import *
class offer_form(forms.ModelForm):
    class Meta:
        model = ad_offer_user
        fields = ["offer_amount"]