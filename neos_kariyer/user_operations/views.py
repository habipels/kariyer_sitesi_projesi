from django.shortcuts import render ,HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import *

# Create your views here.
#Kullanıcı Giriş Bölümü
def user_login(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            #messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"user_operations_temp/login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        #return redirect("index")
    return render(request, "user_operations_temp/login.html",context)
#Kullanını Kayıt Sayfasıdır.
def user_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        newUser = User(username =username,email=email)
        newUser.set_password(password)
        try:
            newUser.save()
            login(request,newUser)
            messages.info(request,"Başarıyla Kayıt Oldunuz...")
            return redirect("/user/membership/3")
        except:
            messages.info(request,"İstediğiniz Kullanıcı Adı Kullanılmaktadır...")
            return redirect("/user/register/")
        
    context = {
            "form" : form
        }
    return render(request,"user_operations_temp/register.html",context)
def user_logout(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
#Kullanıcı Druumlarını Düzenliyip Obje Oluşturulan Yerdir Bağlanti Models.py dir
def membership(request,id):
    if id == 3:
        print("Selamlar")
    elif id == 1:
        z  = user_status.objects.create(durum = 1)
        z.user = request.user
        z.save()
        return redirect("/profile/profil/")
    elif id == 0:
        z  = user_status.objects.create(durum = 0)
        z.user = request.user
        z.save()
        return redirect("/profile/company/")
    return render(request, "user_operations_temp/membership.html")
import random
from django.core.mail import send_mail
def email_gonder(request):
    print("Selam")
    username = request.POST.get('dili')
    mail_alindi = 0
    for i in username:
        if i == "@":
            mail_alindi = 1
            break
    if mail_alindi == 1:
        m = User.objects.filter(email=username)
        for i in m :
            idim = i.id
            mail = i.email
        try:
            ker = parola_sifirla.objects.filter(user_id = idim)
            
            print(ker)
        except:
            ker = 0
        if ker:
            gonder = random.randint(111111, 999999)
            print(gonder)
            parola_sifirla.objects.filter(user_id=idim).update(sifirla = gonder)
            baslik = "Neos Kariyer Parola Sıfırlama"
            s =username+ """ Kullanıcısı 
            Parola Sıfırlma Kodu = """ +str(gonder)
            mail_adresi = mail
            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])
        else:
            gonder = random.randint(111111, 999999)
            parola_sifirla.objects.create(user_id=idim,sifirla = gonder)
            baslik = "Neos Kariyer Parola Sıfırlama"
            s =username+ """ Kullanıcısı 
            Parola Sıfırlma Kodu = """ +str(gonder)
            mail_adresi = mail
            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])
        return redirect("/user/reset/")
    else:
        m = User.objects.filter(username=username)
        for i in m :
            idim = i.id
            mail = i.email
        try:
            ker = parola_sifirla.objects.filter(user_id = idim)
            
            print(ker)
        except:
            ker = 0
        if ker:
            gonder = random.randint(111111, 999999)
            print(gonder)
            parola_sifirla.objects.filter(user_id=idim).update(sifirla = gonder)
            baslik = "Neos Kariyer Parola Sıfırlama"
            s =username+ """ Kullanıcısı 
            Parola Sıfırlma Kodu = """ +str(gonder)
            mail_adresi = mail
            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])
        else:
            gonder = random.randint(111111, 999999)
            parola_sifirla.objects.create(user_id=idim,sifirla = gonder)
            baslik = "Neos Kariyer Parola Sıfırlama"
            s =username+ """ Kullanıcısı 
            Parola Sıfırlma Kodu = """ +str(gonder)
            mail_adresi = mail
            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])
        return redirect("/user/passrest/")
from .forms import passreset
def parola_sifirlama(request,idim,kod):
    form = passreset(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get("password")
        user = User.objects.get(id=idim)
        print(idim)
        if parola_sifirla.objects.filter(user_id = idim,sifirla=kod):
            user.set_password(password)
            user.save()
            messages.success(request, "Parola Sıfırlandı")
            return redirect("/user/login/")
        else:
            messages.success(request, "Kullanıcı Bulunamadı")
            return redirect("/user/reset/")
    return render(request, "user_operations_temp/password_reset.html",{"form":form})

def pass_reset(request):
    if request.POST:
        users = request.POST.get("bilgi")
        print(users)
        kod = request.POST.get("dogrulaemail")
        print(kod)
        mail_alma = 0

        if users and kod :
            print("if 1")
            for i in users:
                if i == "@":
                    mail_alma = 1
                    print("if 2")
                    break
            if mail_alma:
                print("if 3")
                m = User.objects.filter(email=users)
                for i in m:
                    idim = i.id
                user = User.objects.get(id=idim)
                if parola_sifirla.objects.filter(user_id = idim,sifirla=kod):
                    print("kod Doğru",kod)
                    return redirect("/user/reset/"+str(idim)+"/"+str(kod))
                    
            else:
                print("if 3")
                m = User.objects.filter(username=users)
                for i in m:
                    idim = i.id
                user = User.objects.get(id=idim)
                if parola_sifirla.objects.filter(user_id = idim,sifirla=kod):
                    print("kod Doğru",kod)
                    return redirect("/user/reset/"+str(idim)+"/"+str(kod))
        else:   
            print("else 1")
    return render(request, "user_operations_temp/first_pass_reset.html")