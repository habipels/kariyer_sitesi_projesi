from django.shortcuts import render,redirect
from user_operations.models import user_status
from profil.models import *
# Create your views here.
#İndex Sayfasını Barındırı
def home_index(request):
    if request.user.is_authenticated:
        if user_status.objects.filter(user_id = request.user):
            for i in user_status.objects.filter(user = request.user):
                m = i.durum
                ilan_yapma = m
                if m:
                    z = user_profil.objects.filter(user = request.user)
                    for j in z:
                        bakiye = j.bakiye
                else:
                    z = company_profile.objects.filter(user = request.user)
                    for j in z:
                        bakiye = j.bakiye
        else:
            return redirect("/user/membership/3")
    try:
        return render(request, "home_temp/index.html",{"ilan_yapma":ilan_yapma,"bakiye":bakiye})
    except:
        return render(request, "home_temp/index.html")