
from .forms import *
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from offer.models import *
from all_category.models import *
from user_operations.models import user_status
from datetime import date as datetime  ,timedelta
# Create your views here.
#enddate = startdate - timedelta(days=7) +timedelta(days=1)
#startdate = datetime.today() +timedelta(days=7)
#İlan Ekleme Fonksiyonu İcinde Obje Oluşturulur
def addads(request):
    if request.user.is_authenticated:
        if user_status.objects.filter(user_id = request.user):
            pass
        else:
            return redirect("/user/membership/3")
    form = is_ilan(request.POST or None,request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        m = datetime.today() + timedelta(days=7)
        print(m)
        article.ilan_sahibi = request.user
        article.ilan_gecis_tablosu = m
        article.chip_amunt = 0
        article.offer_much = 0

        article.save()
        category_ads.objects.create(ilan_id=article.id,
        aranan_deneyim_id=request.POST.get("cars"),
        lokasyon_id = request.POST.get("lokasyon"),
        ilan_calima_saati_id=request.POST.get("haft"),
        ilan_ucretlendirmesi_id=request.POST.get("ucretlendirmeler"))
        print(request.POST)
        return redirect("/ads/views/"+str(article.id))

    deneyimler = deneyim.objects.all()
    lokasyonlar = lokasyon.objects.all()
    ilan_calisma_saati = kategoriler.objects.all()
    ilan_ucretlendirmesi = ucretlendirme.objects.all()
    sozluk = {"form":form,
    "deneyimler":deneyimler,
    "ilan_calisma_saati":ilan_calisma_saati,
    "ilan_ucretlendirmesi":ilan_ucretlendirmesi,
    "lokasyonlar":lokasyonlar}
    return render(request,"ads_temp/ilan_ekle.html",sozluk)
#İlanların Yönetim Panelidir Ve Sİl Güncelle İçinde Barındırır
def dashboard(request):
    if request.user.is_authenticated:
        if user_status.objects.filter(user_id = request.user):
            pass
        else:
            return redirect("/user/membership/3")
    articles = ads_data.objects.filter(ilan_sahibi = request.user).order_by("-ilan_olusturma_tarihi")
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
            else:
                ads_data.objects.filter(id = i.id).update(chip_amunt = m)
        if i.offer_much == 0:
            ads_data.objects.filter(id = i.id).update(chip_amunt = 0)
    articles = ads_data.objects.filter(ilan_sahibi = request.user).order_by("-ilan_olusturma_tarihi")
    offers = ad_offer_user.objects.order_by("offer_amount")
    context = {
        "articles":articles,
        "offers":offers
        
    }
    return render(request,"ads_temp/dashboard.html",context)
#İlan Güncelleme Sayfasıdır
from django.utils import timezone

def updateads(request,id):
    if request.user.is_authenticated:
        if user_status.objects.filter(user_id = request.user):
            pass
        else:
            return redirect("/user/membership/3")
    article = get_object_or_404(ads_data,id = id)
    ilan = ads_data.objects.filter(id = id)
    for i in ilan:
        suan = i.ilan_gecis_tablosu
    print(type(suan),"selam")
    #now = timezone.now()
    if suan < timezone.now():
        suan =  timezone.now()
    form = is_ilan(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.ilan_gecis_tablosu = suan+ timedelta(days=7)
        category_ads.objects.filter(ilan_id=id).update(
        aranan_deneyim_id=request.POST.get("cars"),
        lokasyon_id = request.POST.get("lokasyon"),
        ilan_calima_saati_id=request.POST.get("haft"),
        ilan_ucretlendirmesi_id=request.POST.get("ucretlendirmeler"))
        article.save()
        
        messages.success(request,"İlan başarıyla güncellendi")
        return redirect("ads:dashboard")

    deneyimler = deneyim.objects.all()
    lokasyonlar = lokasyon.objects.all()
    ilan_calisma_saati = kategoriler.objects.all()
    ilan_ucretlendirmesi = ucretlendirme.objects.all()
    sozluk = {"form":form,
    "deneyimler":deneyimler,
    "ilan_calisma_saati":ilan_calisma_saati,
    "ilan_ucretlendirmesi":ilan_ucretlendirmesi,
    "lokasyonlar":lokasyonlar}
    return render(request,"ads_temp/update.html",sozluk)

#İlan Silme Fonksiyonudur
def ads_delete(request,id):
    if request.user.is_authenticated:
        if user_status.objects.filter(user_id = request.user):
            pass
        else:
            return redirect("/user/membership/3")
    article = get_object_or_404(ads_data,id = id)

    article.delete()

    messages.success(request,"İlan Başarıyla Silindi")

    return redirect("ads:dashboard")
#ilan detay teklif gösterme 
def ads_views_offer(request,id):
    try:
        acik = ad_offer_user.objects.filter(ads_ofer_id = id).order_by("-offer_amount")
        a = ads_data.objects.filter(id = id)
        ads_filter = category_ads.objects.filter(ilan_id = id)
        z = 1
    except:
        pass
    all_profil = user_profil.objects.all()
    print(all_profil)
    data = {"ads":a,"ads_filter":ads_filter,"acik":acik,"z":z,"all_profil":all_profil}
    return render(request, "offer_temp/ads_views.html",data)