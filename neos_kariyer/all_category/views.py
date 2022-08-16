from django.shortcuts import render,redirect

# Create your views here.
from django.core.mail import send_mail


def mail_gonderme(request):
    s = "İşlemler"
    mail_adresi = "habibelis65@gmail.com"
    send_mail("Selam",s,mail_adresi,["habipelis65@gmail.com",mail_adresi])
    return redirect("index")