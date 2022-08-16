from django.shortcuts import render,get_object_or_404,redirect , HttpResponse
from ads.models import *
from .models import *
from datetime import date as datetime  ,timedelta
from django.contrib import messages
from .form import offer_form
from django.contrib import messages
from offer.models import *
from profil.models import *
from django.core.paginator import Paginator
from user_operations.models import user_status
from all_category.models import *
# Create your views here.
#Tekli ilan Gösterme Sayfası 
def ads_show(request,id):
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
    else:
        ilan_yapma = 0
        bakiye = 0
    a = ads_data.objects.filter(id = id)
    ads_filter = category_ads.objects.filter(ilan_id = id)
    all_profil = user_profil.objects.all()
    print(all_profil)
    print(ads_filter)
    try:
        
        ilan_kont =ad_offer_user.objects.filter(offer_user_id = request.user,ads_ofer_id = id)
    except:
        ilan_kont =0 
    if ilan_kont :
        acik = ad_offer_user.objects.filter(ads_ofer_id = id).order_by("-offer_amount")
        
    else:
        acik = 0
    if request.POST.get("teklifmiktari"):
        if ad_offer_user.objects.filter(offer_user = request.user,
            ads_ofer_id = id):
            bakiye_durumu = user_profil.objects.filter(user=request.user)
            for i in bakiye_durumu:
                bak = i.bakiye
            if bak >= 6:
                ad_offer_user.objects.filter(offer_user = request.user,
                ads_ofer_id = id).update(offer_amount = request.POST.get("teklifmiktari"))
                articles = ads_data.objects.filter(ilan_sahibi = id).order_by("-ilan_olusturma_tarihi")
                offers = ad_offer_user.objects.order_by("offer_amount")
                for i in articles:
                    z = 0
                    for j in offers:
                        if i.id == j.ads_ofer_id:
                            z = z+1
                    ads_data.objects.filter(id = i.id).update(offer_much = z)
                    m = 0
                    for j in offers:
                        if i.id == j.ads_ofer_id:
                            m = j.offer_amount 
                            ads_data.objects.filter(id = i.id).update(chip_amunt = m)
                            break 
                bak = bak -6
                bakiye_durumu.update(bakiye=bak)
                messages.success(request,"Daha Önce Teklif Vermiştiniz")
                return redirect("/views/dashboard/")
        else:
            bakiye_durumu = user_profil.objects.filter(user=request.user)
            for i in bakiye_durumu:
                bak = i.bakiye
            if bak >= 6:
                ad_offer_user.objects.create(offer_user = request.user,
                ads_ofer_id = id,offer_amount=request.POST.get("teklifmiktari"),
                acceptance_status = 0,read_status = 0,offer_date = datetime.today() )
                articles = ads_data.objects.filter(ilan_sahibi = id).order_by("-ilan_olusturma_tarihi")
                offers = ad_offer_user.objects.order_by("offer_amount")
                for i in articles:
                    z = 0
                    for j in offers:
                        if i.id == j.ads_ofer_id:
                            z = z+1
                    ads_data.objects.filter(id = i.id).update(offer_much = z)
                    m = 0
                    for j in offers:
                        if i.id == j.ads_ofer_id:
                            m = j.offer_amount 
                            ads_data.objects.filter(id = i.id).update(chip_amunt = m)
                            break
                bak = bak -6
                bakiye_durumu.update(bakiye=bak)
                messages.success(request,"Teklif Verildi")
                articles = ads_data.objects.filter(ilan_sahibi = id).order_by("-ilan_olusturma_tarihi")
                offers = ad_offer_user.objects.order_by("offer_amount")
                return redirect("/views/dashboard/")
            messages.success(request,"Bakiye Yetersiz")
    data = {"ads":a,"ads_filter":ads_filter,"acik":acik,"ilan_yapma":ilan_yapma,"all_profil":all_profil,"bakiye":bakiye}
    return render(request, "offer_temp/ads_views.html",data)
#Tüm İlanları Gösterme SAyfası 
from datetime import date as datetime  ,timedelta
def all_show_ads(request):
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
    else:
        ilan_yapma = 0
        bakiye =0
    kategor = kategoriler.objects.all()
    ad = ads_data.objects.filter(ilan_gecis_tablosu__range=[datetime.today(), "2029-01-31"] )
    lokal = lokasyon.objects.all()
    deneyimler = deneyim.objects.all()
    ads_kategori = category_ads.objects.all()
    if request.GET.get("kategori") and request.GET.get("kategori") !="Tümü":
        secim_kategori = request.GET.get("kategori")
        print(secim_kategori)
    else:
        secim_kategori = "Tümü"
    if request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü":
        secim_sehir = request.GET.get("lokasyon")
        print(secim_sehir)
    else:
        secim_sehir = "Tümü"
    if request.GET.get("deneyim") and request.GET.get("deneyim") !="Tümü":
        secim_deneyim = request.GET.get("deneyim")
        print(secim_deneyim)
    else:
        secim_deneyim = "Tümü"
    if request.GET:
        if request.GET.get("islem") == "0":
            if (request.GET.get("kategori") and request.GET.get("kategori") !="Tümü") and (request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü"):
                for i in kategoriler.objects.all():
                    if secim_kategori == i.kategory_ismi:
                        kategorilerim = i.id
                        
                for i in lokasyon.objects.all():
                    if secim_sehir == i.sehir_ismi:
                        sehirlerim = i.id
                ads_kategori = category_ads.objects.filter(lokasyon_id =sehirlerim,ilan_calima_saati_id=kategorilerim)
                
                kategori_secim = request.GET.get("kategori")
            elif(request.GET.get("kategori") and request.GET.get("kategori") !="Tümü") :
                for i in kategoriler.objects.all():
                    if secim_kategori == i.kategory_ismi:
                        kategorilerim = i.id
                ads_kategori = category_ads.objects.filter(ilan_calima_saati_id=kategorilerim)
            elif(request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü") :
                
                for i in lokasyon.objects.all():
                    if secim_sehir == i.sehir_ismi:
                        sehirlerim = i.id
                        print(sehirlerim)
                ads_kategori = category_ads.objects.filter(lokasyon_id =sehirlerim)
            else:
                pass
            
            if request.GET.get("deneyim") and request.GET.get("deneyim") !="Tümü":
                for i in deneyim.objects.all():
                    if secim_deneyim == i.tecrube:
                        deneyimim = i.id
                        pass
                ads_kategori = category_ads.objects.filter(aranan_deneyim_id =deneyimim)
            
    
    data = {"ads":ad,"ads_kategori":ads_kategori,"ilan_yapma":ilan_yapma,"kategor":kategor,"lokal":lokal,"deneyimler":deneyimler,"bakiye":bakiye}
    return render(request, "offer_temp/all_ads.html",data)
#dashboard
def dashboard(request):
    if request.user.is_authenticated:
        if user_status.objects.filter(user_id = request.user):
            for i in user_status.objects.filter(user = request.user):
                m = i.durum
                ilan_yapma = m
                if m:
                    z = user_profil.objects.filter(user = request.user)
                    for j in z:
                        bakiye = j.bakiye
                    offers = ad_offer_user.objects.filter(offer_user_id = request.user).order_by("-offer_date")
                    print(offers)
                    articles = ads_data.objects.all()
                    offers = ad_offer_user.objects.filter(offer_user_id = request.user).order_by("-offer_date")
                    context = {
                        "articles":articles,
                        "offers":offers,
                        "ilan_yapma":ilan_yapma,"bakiye":bakiye
                    }
                    return render(request,"offer_temp/ads_offer_dashboard.html",context)
                else:
                    z = company_profile.objects.filter(user = request.user)
                    for j in z:
                        bakiye = j.bakiye
                        kategori = kategoriler.objects.all()
                        idim = j.id
                    lokal = lokasyon.objects.all()
                    uzman = user_profil.objects.all()
                    uzman2 = working_condition.objects.all()
                    makale_listesi = uzman
                    page = request.GET.get('sayfa', 1)
                    paginator = Paginator(makale_listesi, 40)
                    deneyimler = deneyim.objects.all()
                    ilana_davet_edilen = call_offer_user_add.objects.all()
                    ilanlarim = ads_data.objects.filter(ilan_sahibi=request.user)
                    calismak_icin_verilen_teklifler = expert.objects.filter(offer_user_id=idim)
                    try:
                        secili_sayfaki_konular = paginator.page(page)
                    except PageNotAnInteger:
                        secili_sayfaki_konular = paginator.page(1)
                    except EmptyPage:
                        secili_sayfaki_konular = paginator.page(paginator.num_pages)
                    
                    content = {"ilanlarim":ilanlarim,"calismak_icin_verilen_teklifler":calismak_icin_verilen_teklifler,"ilana_davet_edilen":ilana_davet_edilen,"bakiye":bakiye,"uzman":secili_sayfaki_konular,"uzman2":uzman2,"kategori":kategori,"lokal":lokal,"deneyimler":deneyimler,"ilan_yapma":ilan_yapma}
                    
                    return render(request,"offer_temp/ads_offer_dashboard.html",content)
        else:
            return redirect("/user/membership/3")
    else:
        ilan_yapma = 0
    
#Teklif Güncelleme 
def update_offer(request,id):
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
    else:
        ilan_yapma = 0
    article = get_object_or_404(ad_offer_user,id = id)
    form = offer_form(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        
        messages.success(request,"Teklif başarıyla güncellendi")
        return redirect("ads:dashboard")


    return render(request,"ads_temp/update.html",{"form":form,"ilan_yapma":ilan_yapma,"bakiye":bakiye})

#Teklif Silme Fonksiyonudur
def offer_delete(request,id):
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
    else:
        ilan_yapma = 0
    article = get_object_or_404(ad_offer_user,id = id)
    article.delete()
    articles = ads_data.objects.filter(ilan_sahibi = id).order_by("-ilan_olusturma_tarihi")
    offers = ad_offer_user.objects.order_by("offer_amount")
    for i in articles:
        z = 0
        for j in offers:
            if i.id == j.ads_ofer_id:
                z = z+1
        ads_data.objects.filter(id = i.id).update(offer_much = z)
        m = 0
        for j in offers:
            if i.id == j.ads_ofer_id:
                m = j.offer_amount 
                ads_data.objects.filter(id = i.id).update(chip_amunt = m)
                break
    messages.success(request,"Teklif Silindi")
        
        
    messages.success(request,"Teklif Başarıyla Silindi")
    return redirect("adsoffer:offerdashboard")

def expert_offer_views(request):
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
    else:
        ilan_yapma = 0
    if request.user.is_authenticated:
        if user_status.objects.filter(user_id = request.user):
            for i in user_status.objects.filter(user = request.user):
                m = i.durum
                ilan_yapma = m
                if m:
                    z = user_profil.objects.filter(user = request.user)
                    for j in z:
                        bakiye = j.bakiye
                        idim = j.id
                    offers = ad_offer_user.objects.filter(offer_user_id = request.user).order_by("-offer_date")
                    print(offers)
                    articles = ads_data.objects.all()
                    offers = ad_offer_user.objects.filter(offer_user_id = request.user).order_by("-offer_date")
                    bana_gelen_istekler = call_offer_user_add.objects.filter(offer_user = idim)
                    bana_gelen_calisma_teklifleri = expert.objects.filter(expert_offers_user_id =request.user)
                    sirketler = company_profile.objects.all()
                    context = {"sirketler":sirketler,
                        "bana_gelen_calisma_teklifleri":bana_gelen_calisma_teklifleri,
                        "bana_gelen_istekler":bana_gelen_istekler,
                        "articles":articles,
                        "offers":offers,
                        "ilan_yapma":ilan_yapma,"bakiye":bakiye
                    }
                    return render(request, "offer_temp/expert_users.html",context)
                else:
                    aldigin_ilan_teklifleri = ad_offer_user.objects.all()
                    ilanlarim = ads_data.objects.filter(ilan_sahibi = request.user)
                    #alinan_uzman_teklifleri = expert.objects.filter(expert_offers_user_id = request.user)
                    kullanici = user_profil.objects.all()
                    content = {
                    "kullanici":kullanici,"aldigin_ilan_teklifleri":aldigin_ilan_teklifleri,
                    "ilanlarim":ilanlarim,"ilan_yapma":ilan_yapma,"bakiye":bakiye
                    }
                    return render(request, "offer_temp/expert_users.html",content)
    aldigin_ilan_teklifleri = ad_offer_user.objects.all()
    ilanlarim = ads_data.objects.filter(ilan_sahibi = request.user)
    #alinan_uzman_teklifleri = expert.objects.filter(expert_offers_user_id = request.user)
    kullanici = user_profil.objects.all()
    content = {
    "kullanici":kullanici,"aldigin_ilan_teklifleri":aldigin_ilan_teklifleri,
    "ilanlarim":ilanlarim,"ilan_yapma":ilan_yapma,"bakiye":bakiye
    }
    return render(request, "offer_temp/expert_users.html",content)
def alinan_uzman_tekliflerini_sil(request,id):
    expert_expert.objects.filter(id = id).delete()
    return redirect("adsoffer:inbox")
def alinan_uzman_tekliflerini_red(request,id):
    expert_expert.objects.filter(id = id).update(veto_status = True)
    return redirect("adsoffer:inbox")
def alinan_uzman_tekliflerini_onayla(request,id):
    expert_expert.objects.filter(id = id).update(acceptance_status = True)
    return redirect("adsoffer:inbox")
def aldigin_ilan_teklifleri_onayla(request,id):
    ad_offer_user.objects.filter(id = id).update(acceptance_status = True)
    return redirect("adsoffer:inbox")
def ilana_davet(request,id,users):
    print(type(users))
    z = company_profile.objects.filter(user = request.user)
    for i in z:
        bakiye = i.bakiye
        bakiye = int(bakiye)
        
      
        if bakiye >= 6:
            bakiye = bakiye -6
            olustur = call_offer_user_add.objects.create(ads_ofer_id=id,offer_user_id = users,acceptance_status=False,read_status=False)

            z.update(bakiye = bakiye)
        else:
            messages.success(request,"Bakiye Yetersiz ")
            return redirect("adsoffer:inbox")
    messages.success(request,"Davete Çağırma Başarılı ")
    return redirect("adsoffer:inbox")
def aldigin_ilan_teklifleri_red(request,id):
    print(request.GET.get("red"+str(id)))
    if request.GET.get("red"+str(id)) == "0":
        teklif_redd.objects.create(adds_offer_id = id ,redd ="Seçilmedi")
    elif request.GET.get("red"+str(id)) == "1":
        teklif_redd.objects.create(adds_offer_id = id ,redd ="Verilen Ücret Yüksek")
    elif request.GET.get("red"+str(id)) == "2":
        teklif_redd.objects.create(adds_offer_id = id ,redd ="Deneyim Düşük")
    elif request.GET.get("red"+str(id)) == "3":
        teklif_redd.objects.create(adds_offer_id = id ,redd ="İlan Yapılmaktan Vazgeçti")
    elif request.GET.get("red"+str(id)) == "4":
        teklif_redd.objects.create(adds_offer_id = id ,redd ="Diğer")
    ad_offer_user.objects.filter(id = id).update(veto_status = True)
    return redirect("adsoffer:inbox")
def aldigin_ilan_teklifleri_sil(request,id):
    ad_offer_user.objects.filter(id = id).delete()
    return redirect("adsoffer:inbox")
def expert_views_all(request):
    
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
    else:
        ilan_yapma = 0
        bakiye = 0
    if request.GET.get("kategori") and request.GET.get("kategori") !="Tümü":
        secim_kategori = request.GET.get("kategori")
        print(secim_kategori)
    else:
        secim_kategori = "Tümü"
    if request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü":
        secim_sehir = request.GET.get("lokasyon")
        
    else:
        secim_sehir = "Tümü"
    if request.GET.get("deneyim") and request.GET.get("deneyim") !="Tümü":
        secim_deneyim = request.GET.get("deneyim")
        
    else:
        secim_deneyim = "Tümü"
    if request.GET:
        if request.GET.get("islem") == "0":
            sirala = request.GET.get("islem")
            if (request.GET.get("kategori") and request.GET.get("kategori") !="Tümü") and (request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü"):
                for i in kategoriler.objects.all():
                    if secim_kategori == i.kategory_ismi:
                        kategorilerim = i.id
                for i in lokasyon.objects.all():
                    if secim_sehir == i.sehir_ismi:
                        sehirlerim = i.id
                uzman = user_profil.objects.filter(user_kategori_id = kategorilerim,lokasyon_id = sehirlerim)
                kategori_secim = request.GET.get("kategori")
            elif(request.GET.get("kategori") and request.GET.get("kategori") !="Tümü") :
                for i in kategoriler.objects.all():
                    if secim_kategori == i.kategory_ismi:
                        kategorilerim = i.id
                
                uzman = user_profil.objects.filter(user_kategori_id = kategorilerim)
            elif(request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü") :
                
                for i in lokasyon.objects.all():
                    if secim_sehir == i.sehir_ismi:
                        sehirlerim = i.id
                        print(sehirlerim)
                uzman = user_profil.objects.filter(lokasyon_id = sehirlerim)
            else:
                uzman = user_profil.objects.all()
            
            if request.GET.get("deneyim") and request.GET.get("deneyim") !="Tümü":
                for i in deneyim.objects.all():
                    if secim_deneyim == i.tecrube:
                        deneyimim = i.id
                    
                uzman2=working_condition.objects.filter(deneyim_id = deneyimim)
            else:
                uzman2=working_condition.objects.filter()
            kategori = kategoriler.objects.all()
            lokal = lokasyon.objects.all()
            deneyimler = deneyim.objects.all()
            
            content = {"bakiye":bakiye,"uzman":uzman,"uzman2":uzman2,"kategori":kategori,"lokal":lokal,"deneyimler":deneyimler,"ilan_yapma":ilan_yapma,"secim_kategori":secim_kategori,"secim_sehir":secim_sehir,"secim_deneyim":secim_deneyim}
            return render(request, "profil_temp/all_profile_views.html",content)
        
        if request.GET.get("islem") == "1":
            sirala = request.GET.get("islem")
            if (request.GET.get("kategori") and request.GET.get("kategori") !="Tümü") and (request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü"):
                for i in kategoriler.objects.all():
                    if secim_kategori == i.kategory_ismi:
                        kategorilerim = i.id
                for i in lokasyon.objects.all():
                    if secim_sehir == i.sehir_ismi:
                        sehirlerim = i.id
                uzman = user_profil.objects.filter(user_kategori_id = kategorilerim,lokasyon_id = sehirlerim)
                kategori_secim = request.GET.get("kategori")
            elif(request.GET.get("kategori") and request.GET.get("kategori") !="Tümü") :
                for i in kategoriler.objects.all():
                    if secim_kategori == i.kategory_ismi:
                        kategorilerim = i.id
                
                uzman = user_profil.objects.filter(user_kategori_id = kategorilerim)
            elif(request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü") :
                
                for i in lokasyon.objects.all():
                    if secim_sehir == i.sehir_ismi:
                        sehirlerim = i.id
                        print(sehirlerim)
                uzman = user_profil.objects.filter(lokasyon_id = sehirlerim)
            else:
                uzman = user_profil.objects.all()
            
            if request.GET.get("deneyim") and request.GET.get("deneyim") !="Tümü":
                for i in deneyim.objects.all():
                    if secim_deneyim == i.tecrube:
                        deneyimim = i.id
                    
                uzman2=working_condition.objects.filter(deneyim_id = deneyimim).order_by("-deneyim_id")
            else:
                uzman2=working_condition.objects.filter().order_by("-deneyim_id")
            kategori = kategoriler.objects.all()
            lokal = lokasyon.objects.all()
            deneyimler = deneyim.objects.all()
            
            content = {"bakiye":bakiye,"uzman":uzman,"uzman2":uzman2,"kategori":kategori,"lokal":lokal,"deneyimler":deneyimler,"ilan_yapma":ilan_yapma,"secim_kategori":secim_kategori,"secim_sehir":secim_sehir,"secim_deneyim":secim_deneyim}
            return render(request, "profil_temp/all_profile_views.html",content)
        if request.GET.get("islem") == "2":
            sirala = request.GET.get("islem")
            if (request.GET.get("kategori") and request.GET.get("kategori") !="Tümü") and (request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü"):
                for i in kategoriler.objects.all():
                    if secim_kategori == i.kategory_ismi:
                        kategorilerim = i.id
                for i in lokasyon.objects.all():
                    if secim_sehir == i.sehir_ismi:
                        sehirlerim = i.id
                uzman = user_profil.objects.filter(user_kategori_id = kategorilerim,lokasyon_id = sehirlerim)
                kategori_secim = request.GET.get("kategori")
            elif(request.GET.get("kategori") and request.GET.get("kategori") !="Tümü") :
                for i in kategoriler.objects.all():
                    if secim_kategori == i.kategory_ismi:
                        kategorilerim = i.id
                
                uzman = user_profil.objects.filter(user_kategori_id = kategorilerim)
            elif(request.GET.get("lokasyon") and request.GET.get("lokasyon") !="Tümü") :
                
                for i in lokasyon.objects.all():
                    if secim_sehir == i.sehir_ismi:
                        sehirlerim = i.id
                        print(sehirlerim)
                uzman = user_profil.objects.filter(lokasyon_id = sehirlerim)
            else:
                uzman = user_profil.objects.all()
            
            if request.GET.get("deneyim") and request.GET.get("deneyim") !="Tümü":
                for i in deneyim.objects.all():
                    if secim_deneyim == i.tecrube:
                        deneyimim = i.id
                    
                uzman2=working_condition.objects.filter(deneyim_id = deneyimim).order_by("deneyim_id")
            else:
                uzman2=working_condition.objects.filter().order_by("deneyim_id")
            kategori = kategoriler.objects.all()
            lokal = lokasyon.objects.all()
            deneyimler = deneyim.objects.all()
            
            content = {"bakiye":bakiye,"uzman":uzman,"uzman2":uzman2,"kategori":kategori,"lokal":lokal,"deneyimler":deneyimler,"ilan_yapma":ilan_yapma,"secim_kategori":secim_kategori,"secim_sehir":secim_sehir,"secim_deneyim":secim_deneyim}
            return render(request, "profil_temp/all_profile_views.html",content)
    
    kategori = kategoriler.objects.all()
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
    
    content = {"bakiye":bakiye,"uzman":secili_sayfaki_konular,"uzman2":uzman2,"kategori":kategori,"lokal":lokal,"deneyimler":deneyimler,"ilan_yapma":ilan_yapma,"secim_kategori":secim_kategori,"secim_sehir":secim_sehir,"secim_deneyim":secim_deneyim}
    return render(request, "profil_temp/all_profile_views.html",content)

#tüm kullanıcıların teklif verme yeridir
def offer_alluser(id,durum,teklifmiktari,teklifeden):
    if durum:
        z =expert_expert.objects.create(expert_offers_user_id = id,
        offer_user_id=teklifeden,acceptance_status = False,read_status = False,offer_amount = teklifmiktari)
        
        
    else:
        z = expert.objects.create(expert_offers_user_id = id,
        offer_user_id =teklifeden,acceptance_status = False,read_status = False,offer_amount = teklifmiktari)
        
        
    