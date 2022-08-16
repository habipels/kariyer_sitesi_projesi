from django.contrib import admin
from django.urls import path
from . import views

app_name = "adsoffer"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "offerdashboard"),
    path('adsshow/<int:id>',views.ads_show,name = "adsshow"),
    path('allads/',views.all_show_ads,name = "allads"),
    path('offerdelete/<int:id>',views.offer_delete,name = "offer_delete"),
    path('inbox/',views.expert_offer_views,name = "inbox"),
    path('allexpert/',views.expert_views_all,name = "allexpert"),
    path('delete/<int:id>',views.alinan_uzman_tekliflerini_sil,name = "alinan_uzman_tekliflerini_sil"),
    path('ilandavet/<int:id>/<int:users>',views.ilana_davet,name = "ilan_davet"),
    path('veto/<int:id>',views.alinan_uzman_tekliflerini_red,name = "alinan_uzman_tekliflerini_red"),
    path('onayla/<int:id>',views.alinan_uzman_tekliflerini_onayla,name = "alinan_uzman_tekliflerini_onayla"),
    path('deletet/<int:id>',views.aldigin_ilan_teklifleri_sil,name = "aldigin_ilan_teklifleri_sil"),
    path('vetot/<int:id>',views.aldigin_ilan_teklifleri_red,name = "aldigin_ilan_teklifleri_red"),
    path('onaylat/<int:id>',views.aldigin_ilan_teklifleri_onayla,name = "aldigin_ilan_teklifleri_onayla"),
]
