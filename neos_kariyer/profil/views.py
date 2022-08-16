from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from all_category.models import *
from ads.models import *
from .forms import *
from user_operations.models import *
from django.contrib import messages
from profil.models import degerlendirme
import random
from django.core.mail import send_mail
from offer.models import *
# Create your views here.
#Uzmanın Kendi profilini Göreceği Yerdir.
def master_user_profile(request):
    if request.user.is_authenticated:
        if user_status.objects.filter(user = request.user):
            for i in user_status.objects.filter(user = request.user):
                m = i.durum
                if m:
                    if user_profil.objects.filter(user= request.user):
                        if working_condition.objects.filter(user = request.user):
                            pass
                        else:
                            working_condition.objects.create(user = request.user)
                    else:
                        user_profil.objects.create(user = request.user,bakiye=50,degerlendirme_puanli=0)
                else:
                    return redirect("profile:company")
                if m:
                    uzman_pr = user_profil.objects.filter(user = request.user)
                    for j in uzman_pr:
                        mail = j.email
            if dogrulama.objects.filter(user = request.user):
                tiplemeler = dogrulama.objects.filter(user=request.user)
                for i in tiplemeler:
                    if i.mail:
                        pass
                    else:
                        if mail_dogrulama.objects.filter(user = request.user):
                            tamam = 1
                            if request.GET.get("dogrulaemail"):
                                for k in mail_dogrulama.objects.filter(user=request.user):
                                    print(type(request.GET.get("dogrulaemail")),type(k.mail))
                                    if request.GET.get("dogrulaemail") == str(k.mail):
                                        dogrulama.objects.filter(user=request.user).update(mail = True)
                                        tamam = 0
                            if tamam:
                                gonder = random.randint(111111, 999999)
                                mail_dogrulama.objects.filter(user=request.user).update(mail = gonder)
                                baslik = "Neos Kariyer"
                                s = "E-posta Doğrulama Kodu = " +str(gonder)
                                mail_adresi = mail
                                send_mail(baslik,s,mail_adresi,[mail,mail_adresi])

                        else:
                            gonder = random.randint(111111, 999999)
                            mail_dogrulama.objects.create(user=request.user,mail = gonder)
                            baslik = "Neos Kariyer"
                            s = "E-posta Doğrulama Kodu = " +str(gonder)
                            mail_adresi = mail
                            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])

            else:
                dogrulama.objects.create(user = request.user,mail = 0,telefon = 0)
                tiplemeler = dogrulama.objects.filter(user=request.user)
                for i in tiplemeler:
                    if i.mail:
                        pass
                    else:
                        if mail_dogrulama.objects.filter(user = request.user):
                            gonder = random.randint(111111, 999999)
                            mail_dogrulama.objects.filter(user=request.user).update(mail = gonder)
                            baslik = "Neos Kariyer"
                            s = "E-posta Doğrulama Kodu = " +str(gonder)
                            mail_adresi = mail
                            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])

                        else:
                            gonder = random.randint(111111, 999999)
                            mail_dogrulama.objects.create(user=request.user,mail = gonder)
                            baslik = "Neos Kariyer"
                            s = "E-posta Doğrulama Kodu = " +str(gonder)
                            mail_adresi = mail
                            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])


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

            if m:
                if user_profil.objects.filter(user= request.user):
                    if working_condition.objects.filter(user = request.user):
                        pass
                    else:
                        working_condition.objects.create(user = request.user)
                else:
                    user_profil.objects.create(user = request.user,bakiye=0)
            else:
                pass
        else:
            return redirect("/user/membership/3")
    kontrol = user_status.objects.filter(user_id = request.user)
    z = 0
    for i in kontrol:
        if i.durum == True:
            z = 1
    if z:

        if request.POST.get("isim_soyisim"):
            k = request.POST.get("isim_soyisim")
            m = user_profil.objects.filter(user_id = request.user).update(isim_soyisim = k )

        if request.POST.get("telefon_numarasi"):
            k = request.POST.get("telefon_numarasi")
            m = user_profil.objects.filter(user_id = request.user).update(telefon = k )
        if request.POST.get("email"):
            k = request.POST.get("email")
            m = user_profil.objects.filter(user_id = request.user).update(email = k )
        article = user_profil.objects.get(user_id = request.user)
        profil_form = user_profile_img(request.POST or None,request.FILES or None,instance = article)
        back_form = user_back_img(request.POST or None,request.FILES or None,instance = article)
        if profil_form.is_valid():
            z = profil_form.save(commit=False)
            z.user= request.user
            z.save()

        if back_form.is_valid():
            z = back_form.save(commit=False)
            z.user= request.user
            z.save()
        hakkimda = get_object_or_404(user_profil,user_id = request.user)
        form = long_dec(request.POST or None,request.FILES or None,instance = hakkimda)
        if form.is_valid():
            hakkimda  = form.save(commit=False)
            hakkimda.user = request.user
            hakkimda.save()
            return redirect("profile:profile")
        if request.POST.get("tarih"):
            z = resume.objects.create(baslik = request.POST.get("isim"),aciklama = request.POST.get("acikla"),tarih = request.POST.get("tarih"))
            z.user_id = request.user
            z.save()
            y = resume.objects.filter(user_id = request.user).order_by("-tarih")
            for j,i in enumerate(y):
                if j % 2== 0:
                    resume.objects.filter(id = i.id).update(yon = "l")
                else:
                    resume.objects.filter(id = i.id).update(yon = "r")

        try:
            z = user_profil.objects.filter(user_id = request.user.id)
            is_bilgisi = working_condition.objects.filter(user_id = request.user)
            user_bilgi = resume.objects.filter(user = request.user).order_by("tarih")
            sozluk = {"bilgiler":user_bilgi,"bilgi":z,"is_bilgisi":is_bilgisi,"profil_form":profil_form,
            "back_form":back_form,"tecrubee":deneyim.objects.all(),"form":form,
            "yetenekleri":abilities.objects.filter(user = request.user),
            "ilan_yapma":ilan_yapma,"bakiye":bakiye}
            return render(request, "profil_temp/master_profil.html",sozluk)
        except:
            return render(request, "profil_temp/master_profil.html",{"bilgi":z,"profil_form":profil_form,"back_form":back_form,"tecrubee":deneyim.objects.all(),"yetenekleri":abilities.objects.filter(user = request.user),"ilan_yapma":ilan_yapma,"bakiye":bakiye})

        return render(request, "profil_temp/master_profil.html",{"profil_form":profil_form,"yetenekleri":abilities.objects.filter(user = request.user),"back_form":back_form,"tecrubee":deneyim.objects.all(),"bakiye":bakiye})
    else:
        return redirect("profile:company")
#Profil Edit sayfası Burasıdır.
def profil_edit(request):
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
    if working_condition.objects.filter(user_id = request.user.id):
        kategori = kategoriler.objects.all()
        konum = lokasyon.objects.all()
        tecrube = deneyim.objects.all()
        saat = calisma_saati.objects.all()
        calisma_durumu = current_situation.objects.all()
        arayis = is_beklentisi.objects.all()
        sozluk = {"kategori":kategori,"konum":konum,"tecrubem":tecrube,"saat":saat,"calisma_durumum":calisma_durumu,"arayis":arayis,"ilan_yapma":ilan_yapma,"bakiye":bakiye}
        if request.POST.get("kategori"):
            k = request.POST.get("kategori")
            m = user_profil.objects.filter(user_id = request.user.id).update(user_kategori_id = k )

        if request.POST.get("w3review"):
            k = request.POST.get("w3review")
            m = user_profil.objects.filter(user_id = request.user.id).update(on_bilgi = k )
        if request.POST.get("sehir"):
            k = request.POST.get("sehir")
            m = user_profil.objects.filter(user_id = request.user.id).update(lokasyon_id = k )
        if request.POST.get("r"):
            k = request.POST.get("r")
            m = working_condition.objects.filter(user_id = request.user.id).update(deneyim_id = k )
        if request.POST.get("t"):
            k = request.POST.get("t")
            m = working_condition.objects.filter(user_id = request.user.id).update(calisma_id = k )
        if request.POST.get("work"):
            k = request.POST.get("work")
            m = working_condition.objects.filter(user_id = request.user.id).update(calisma_durumu_id = k )
        if request.POST.get("is"):
            k = request.POST.get("is")
            m = working_condition.objects.filter(user_id = request.user.id).update(is_b_id = k )
            return redirect("profile:profile")
        return render(request, "profil_temp/profil_edit.html",sozluk)
    else:
        working_condition.objects.create(user_id = request.user.id)
        return redirect("/profile/profiledit/")
#şirket edit
def master_company_profile(request):
    if request.user.is_authenticated:
        if user_status.objects.filter(user_id = request.user):
            for i in user_status.objects.filter(user = request.user):
                m = i.durum
                ilan_yapma = m
                print(m)
                if m:
                    z = company_profile.objects.filter(user_id = request.user)
                    for j in z:
                        bakiye = j.bakiye
                        mail = j.company_email
                else:
                    if company_profile.objects.filter(user= request.user):
                            pass
                    else:
                        company_profile.objects.create(user= request.user,company_email = request.user.email)
                    z = company_profile.objects.filter(user_id = request.user)
                    for j in z:
                        bakiye = j.bakiye
                        mail = j.company_email
                print(mail,"selam")
            print("durumlar")
            if dogrulama.objects.filter(user = request.user) :
                tiplemeler = dogrulama.objects.filter(user=request.user)
                for i in tiplemeler:
                    if i.mail:
                        pass
                    else:
                        if mail_dogrulama.objects.filter(user = request.user):
                            tamam = 1
                            if request.GET.get("dogrulaemail"):
                                for k in mail_dogrulama.objects.filter(user=request.user):
                                    print(type(request.GET.get("dogrulaemail")),type(k.mail))
                                    if request.GET.get("dogrulaemail") == str(k.mail):
                                        dogrulama.objects.filter(user=request.user).update(mail = True)
                                        tamam = 0
                            if tamam:
                                gonder = random.randint(111111, 999999)
                                mail_dogrulama.objects.filter(user=request.user).update(mail = gonder)
                                baslik = "Neos Kariyer"
                                s = "E-posta Doğrulama Kodu = " +str(gonder)
                                mail_adresi = mail
                                send_mail(baslik,s,mail_adresi,[mail,mail_adresi])

                        else:
                            gonder = random.randint(111111, 999999)
                            mail_dogrulama.objects.create(user=request.user,mail = gonder)
                            baslik = "Neos Kariyer"
                            s = "E-posta Doğrulama Kodu = " +str(gonder)
                            mail_adresi = mail
                            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])

            else:
                dogrulama.objects.create(user = request.user,mail = 0,telefon = 0)
                tiplemeler = dogrulama.objects.filter(user=request.user)
                for i in tiplemeler:
                    if i.mail:
                        pass
                    else:
                        if mail_dogrulama.objects.filter(user = request.user):
                            gonder = random.randint(111111, 999999)
                            mail_dogrulama.objects.filter(user=request.user).update(mail = gonder)
                            baslik = "Neos Kariyer"
                            s = "E-posta Doğrulama Kodu = " +str(gonder)
                            mail_adresi = mail
                            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])

                        else:
                            gonder = random.randint(111111, 999999)
                            mail_dogrulama.objects.create(user=request.user,mail = gonder)
                            baslik = "Neos Kariyer"
                            s = "E-posta Doğrulama Kodu = " +str(gonder)
                            mail_adresi = mail
                            send_mail(baslik,s,mail_adresi,[mail,mail_adresi])

        else:
            return redirect("/user/membership/3")
    
    if request.POST.get("acikla"):
        company_profile.objects.filter(user_id = request.user).update(company_explanation = request.POST.get("acikla"))
    if request.POST.get("tarih"):
        company_profile.objects.filter(user_id = request.user).update(company_foundation_year = request.POST.get("tarih"))
    if request.POST.get("kategori"):
        company_profile.objects.filter(user_id = request.user).update(user_kategori_id = request.POST.get("kategori"))
    if request.POST.get("sirketisim"):
        company_profile.objects.filter(user_id = request.user).update(company_name = request.POST.get("sirketisim"))
    if request.POST.get("sirkettelefon"):
        company_profile.objects.filter(user_id = request.user).update(company_telefon = request.POST.get("sirkettelefon"))
    if request.POST.get("sirketemail"):
        company_profile.objects.filter(user_id = request.user).update(company_email = request.POST.get("sirketemail"))
    article = company_profile.objects.get(user_id = request.user)

    profil_form = user_profile_img(request.POST or None,request.FILES or None,instance = article)
    back_form = user_back_img(request.POST or None,request.FILES or None,instance = article)
    kategori = kategoriler.objects.all()

    hakkimda = get_object_or_404(company_profile,user_id = request.user)
    form = long_dec(request.POST or None,request.FILES or None,instance = hakkimda)
    if form.is_valid():
        hakkimda  = form.save(commit=False)
        hakkimda.user = request.user
        hakkimda.save()
        return redirect("profile:company")
    if profil_form.is_valid():
        z = profil_form.save(commit=False)
        z.user= request.user
        z.save()
        return redirect("profile:company")

    if back_form.is_valid():
        z = back_form.save(commit=False)
        z.user= request.user
        z.save()
        return redirect("profile:company")

    try:
        z = company_profile.objects.filter(user_id = request.user)
    except:
        z = 0
    if z :
        z = company_profile.objects.filter(user_id = request.user)
        return render(request, "profil_temp/company_profile.html",{"bilgiler":z,"profil_form":profil_form,"back_form":back_form,"kategori":kategori,"form":form,"ilan_yapma":ilan_yapma,"bakiye":bakiye})
    else:
        return render(request, "profil_temp/company_profile.html",{"profil_form":profil_form,"back_form":back_form,"kategori":kategori,"form":form,"ilan_yapma":ilan_yapma,"bakiye":bakiye})

from offer.views import offer_alluser
def profil_show(request,id):
    if request.user.is_authenticated:
        if user_status.objects.filter(user_id = request.user):
            for i in user_status.objects.filter(user = request.user):
                m = i.durum
                ilan_yapma = m
            for i in user_status.objects.filter(user = request.user):
                m = i.durum
                ilan_yapma = m
                if m:
                    z = user_profil.objects.filter(user = request.user)
                    for j in z:
                        bakiye = j.bakiye
                else:
                    z = company_profile.objects.filter(user = request.user)
                    davetlerim = call_offer_user_add.objects.filter(offer_user_id = id)
                    ilanlarim = ads_data.objects.filter(ilan_sahibi=request.user)
                    for j in z:
                        bakiye = j.bakiye
        davetlerim = 0
        ilanlarim = 0
    else:
        bakiye = 0
        ilan_yapma = 0
        davetlerim = 0
        ilanlarim = 0
    deger = degerlendirme.objects.filter(profil_id = id )
    toplam=0
    toplam_puan = 0
    for i in deger:
        toplam = toplam+ 1
    z = user_profil.objects.filter(id = id)
    for i in z:
        toplam_puan += i.degerlendirme_puanli
        idim = i.id
    yeteneklerim = abilities.objects.filter(user_id = idim)
    if toplam==0 or toplam_puan == 0:
        toplam=0
        toplam_puan = 0
    else:
        toplam_puan = toplam_puan/toplam
        toplam_puan = round(toplam_puan,1)
    if request.POST.get("vehicle2"):
        m = degerlendirme.objects.filter(user = request.user,profil_id = id )

        y = 0
        for i in m :
            y = i.puan

        degerlendirme.objects.filter(user = request.user,profil_id = id ).delete()

        z = user_profil.objects.filter(id = id)
        for i in z:
            b = i.degerlendirme_puanli
            idim = i.id

        b = b - y
        z.update(degerlendirme_puanli = b)
        degerlendirme.objects.filter(user = request.user,profil_id = id).delete()
        degerlendirme_puan_ekle(request.user,id,request.POST.get("vehicle2"))
    for i in z:
        m = i.user_id
    is_bilgisi = working_condition.objects.filter(user = m)
    user_bilgi = resume.objects.filter(user = m).order_by("tarih")
    try:
        degerlendirme_durumu = degerlendirme.objects.filter(user=request.user,profil_id = id)
    except:
        degerlendirme_durumu = None
    if request.POST.get("vehicle1"):
        degerlendirme_puan_ekle(request.user.id, id, request.POST.get("vehicle1") )
    if request.POST.get("teklifleri"):
        durumlar = user_status.objects.filter(user = request.user)
        for i in durumlar:
            k = i.durum
        if company_profile.objects.filter(user = request.user):
            for i in company_profile.objects.filter(user = request.user):
                y = i.id
            mik = company_profile.objects.filter(user = request.user)
            for fil in mik:
                bakiye = fil.bakiye
                bakiye = int(bakiye)
                if bakiye >= 6:
                    bakiye = bakiye -6
                    offer_alluser(m, k, request.POST.get("teklifleri"), y)
                    mik.update(bakiye = bakiye)
                    return redirect("adsoffer:offerdashboard")
                else:
                    messages.success(request,"Bakiye Yetersiz ")


        #offer_alluser(m, k, request.POST.get("teklifleri"), y)
    try:
        if profil_acma.objects.filter(user_id = request.user ,profil_id = id):
            ac = 1
        else:
            ac = 0
    except:
        ac = 0
    sozluk = {"bilgiler":user_bilgi,"bilgi":z,"is_bilgisi":is_bilgisi,
    "ac":ac,"yeteneklerim":yeteneklerim,"degerlendirme_durumu":degerlendirme_durumu,"toplam_puan":toplam_puan,
    "toplam":toplam,"ilan_yapma":ilan_yapma,"bakiye":bakiye,
    "davetlerim":davetlerim,"ilanlarim":ilanlarim}
    return render(request, "profil_temp/user_show_t.html",sozluk)

def prof_ac(request,id):
    #two user profile open
    for i in user_status.objects.filter(user = request.user):
        m = i.durum
        if m:
            z = user_profil.objects.filter(user = request.user)
            for i in z:
                bakiye = i.bakiye
            bakiye = int(bakiye)
            if bakiye >= 6:
                bakiye = bakiye -6
                profil_acma.objects.create(user= request.user,profil_id = id)
                z.update(bakiye = bakiye)
            else:
                messages.success(request,"Bakiye Yetersiz ")
                return redirect("/profile/showprofile/"+str(id))
        else:
            z = company_profile.objects.filter(user = request.user)
            for i in z:
                bakiye = i.bakiye
            bakiye = int(bakiye)
            if bakiye >= 6:
                bakiye = bakiye -6
                profil_acma.objects.create(user= request.user,profil_id = id)
                z.update(bakiye = bakiye)
            else:
                messages.success(request,"Bakiye Yetersiz ")
                return redirect("/profile/showprofile/"+str(id))
    messages.success(request,"Profil Bilgilerini Açma Başarılı")
    return redirect("/profile/showprofile/"+str(id))
from django.http.response import JsonResponse
def programlama_di(request):
    print("selam")
    if 'term' in request.GET:

        kate = programlama_dili.objects.all().values()
        kategori = list()
        c = str(request.GET.get('term'))

        for i in kate:
            if c.upper() == str(i["dil"][0:len(request.GET.get('term'))]):

                kategori.append(i["dil"])
        return JsonResponse(kategori,safe=False)

def ozgecmis_sil(request,id):

    article = get_object_or_404(resume,id = id)
    article.delete()

    return redirect("/profile/profil/")

def yetenek_olusturma(request):


    dili = request.POST.get('dili')
    duzey = request.POST.get('duzey')
    print(dili,duzey)
    if programlama_dili.objects.filter(dil = dili):

        s = programlama_dili.objects.filter(dil = dili)
        for i in s:
            o= i.id

        print(o)
        for i in abilities.objects.all():
            y = i.id
        print(abilities.objects.filter(user_id =request.user,yetenek_dil_id=o))
        if abilities.objects.filter(user_id =request.user,yetenek_dil_id=o):
            print(dili,duzey)
            print(dili,duzey)

        else:
            z = abilities.objects.create(
            user = request.user)
            abilities.objects.filter(user_id =request.user,id = z.id).update(yetenek_dil=o)
            abilities.objects.filter(user_id =request.user,id = z.id).update(deneyimler=duzey)
    return redirect("/profile/profil/")

def yetenek_sil(request):
    if request.method == 'POST':

        id = request.POST.get('id')
        article = get_object_or_404(abilities,id = id)
        article.delete()
        return redirect("/profile/profil/")

def fav_user_ekle (request):
    if request.method == 'POST':

        id = request.POST.get('id')
        print("Eklendi fav",id)
        if fav_user.objects.filter(expert_offers_user=request.user,offer_user_id = id):
            pass
        else:
            fav_user.objects.create(expert_offers_user=request.user,offer_user_id = id)
        return redirect("/profile/profil/")
def fav_ilan_ekle (request):
    if request.method == 'POST':

        id = request.POST.get('id')
        print("Eklendi fav",id)
        if fav_adds.objects.filter(expert_offers_user=request.user,ads_ofer_id = id):
            pass
        else:
            fav_adds.objects.create(expert_offers_user=request.user,ads_ofer_id = id)
        return redirect("/profile/profil/")
def fav_ilan_sil (request):
    if request.method == 'POST':

        id = request.POST.get('id')
        print("Eklendi fav",id)
        if fav_adds.objects.filter(expert_offers_user=request.user,ads_ofer_id = id):
            fav_adds.objects.filter(expert_offers_user=request.user,ads_ofer_id = id).delete()
        else:
            fav_adds.objects.create(expert_offers_user=request.user,ads_ofer_id = id)

        return redirect("/profile/favorilerim/")
def fav_user_sil (request):
    if request.method == 'POST':

        id = request.POST.get('id')
        print("Eklendi fav",id)
        if fav_user.objects.filter(expert_offers_user=request.user,offer_user_id = id):
            fav_user.objects.filter(expert_offers_user=request.user,offer_user_id = id).delete()
        else:
            fav_user.objects.create(expert_offers_user=request.user,offer_user_id = id)

        return redirect("/profile/favorilerim/")
#şirket Sayfasını Göster
def company_show(request,id):
    ilan = ads_data.objects.filter(id = id)
    z = 0
    gelen_id = 0
    for i in ilan:
        gelen_id = i.ilan_sahibi_id
    durumlar = user_status.objects.filter(user_id = gelen_id)
    for i in durumlar:
        z = i.durum
    if z :
        bilgiler = company.objects.filter(user_id = gelen_id)
        is_bilgisi = working_condition.objects.filter(user_id = gelen_id)
        bilgi = resume.objects.filter(user = gelen_id).order_by("tarih")
        sozluk = {"bilgiler":bilgi,"bilgi":bilgiler,"is_bilgisi":is_bilgisi}
        return render(request, "profil_temp/user_show_t.html",sozluk)
    else:
        sirket = company_profile.objects.filter(user_id = gelen_id)
        return render(request, "profil_temp/company_show.html",{"bilgiler":sirket})
def company_showw(request,id):
    gelen_id = id
    durumlar = user_status.objects.filter(user_id = gelen_id)
    for i in durumlar:
        z = i.durum
    if z :
        bilgiler = user_profil.objects.filter(user_id = gelen_id)
        is_bilgisi = working_condition.objects.filter(user_id = gelen_id)
        bilgi = resume.objects.filter(user = gelen_id).order_by("tarih")
        sozluk = {"bilgiler":bilgi,"bilgi":bilgiler,"is_bilgisi":is_bilgisi}
        return render(request, "profil_temp/user_show_t.html",sozluk)
    else:
        sirket = company_profile.objects.filter(user_id = gelen_id)
        return render(request, "profil_temp/company_show.html",{"bilgiler":sirket})

#değerlendirme puanları
def degerlendirme_puan_ekle(user,id,puan):
    z = degerlendirme.objects.create(puan=puan,user_id = user,profil_id = id )
    m = user_profil.objects.filter(id = id)
    print(m)
    for i in m :
        prof = i.degerlendirme_puanli
        r = i.id
    prof = prof +int(puan)
    m.update(degerlendirme_puanli = prof)
    return redirect("/profile/showprofile/"+str(r))

def degerlendirme_sil(request,id):
    m = degerlendirme.objects.filter(id = id )

    y = 0
    for i in m :
        y = i.puan
        adam_id = i.profil_id
    degerlendirme.objects.filter(id = id ).delete()
    print()
    z = user_profil.objects.filter(id = adam_id)
    for i in z:
        b = i.degerlendirme_puanli

    b = b - y
    z.update(degerlendirme_puanli = b)
    return redirect("/profile/showprofile/"+str(adam_id))
from django.core.paginator import Paginator
def degerlendirme_guncelle(user,id,puan):
    return 0


def favorilerim(request):
    for i in user_status.objects.filter(user = request.user):
                m = i.durum
                ilan_yapma = m
                if m:
                    z = user_profil.objects.filter(user = request.user)
                    for j in z:
                        bakiye = j.bakiye
                    all_ads = fav_adds.objects.filter(expert_offers_user = request.user)
                    kategor = kategoriler.objects.all()
                    ad = ads_data.objects.all()
                    lokal = lokasyon.objects.all()
                    deneyimler = deneyim.objects.all()
                    ads_kategori = category_ads.objects.all()
                    data = {"all_ads":all_ads,"ads":ad,"ads_kategori":ads_kategori,"ilan_yapma":ilan_yapma,"kategor":kategor,"lokal":lokal,"deneyimler":deneyimler,"bakiye":bakiye}
                    return render(request, "profil_temp/favorilerim.html",data)
                else:
                    z = company_profile.objects.filter(user = request.user)
                    kategori = kategoriler.objects.all()
                    all_users = fav_user.objects.filter(expert_offers_user = request.user)
                    lokal = lokasyon.objects.all()
                    uzman = user_profil.objects.all()
                    uzman2 = working_condition.objects.all()
                    makale_listesi = uzman
                    page = request.GET.get('sayfa', 1)
                    paginator = Paginator(makale_listesi, 40)
                    deneyimler = deneyim.objects.all()

                    try:
                        secili_sayfaki_konular = paginator.page(page)
                    except PageNotAnInteger:
                        secili_sayfaki_konular = paginator.page(1)
                    except EmptyPage:
                        secili_sayfaki_konular = paginator.page(paginator.num_pages)


                    for j in z:
                        bakiye = j.bakiye
                    content = {"bakiye":bakiye,"uzman":secili_sayfaki_konular,"uzman2":uzman2,"kategori":kategori,"lokal":lokal,"deneyimler":deneyimler,"ilan_yapma":ilan_yapma,"all_users":all_users}
                    return render(request, "profil_temp/favorilerim.html",content)