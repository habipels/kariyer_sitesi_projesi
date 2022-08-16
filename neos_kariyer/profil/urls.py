from django.contrib import admin
from django.urls import path
from . import views

app_name = "profile"

urlpatterns = [
    path('profil/',views.master_user_profile,name = "profile"),
    path('profiledit/',views.profil_edit,name = "profiledit"),
    path('company/',views.master_company_profile,name = "company"),
    path('ozgecmis/<int:id>',views.ozgecmis_sil,name = "ozgecmis_sil"),
    path('openprofile/<int:id>',views.prof_ac,name = "profilac"),
    path('showprofile/<int:id>',views.profil_show,name = "profileshow"),
    path('userprofile/<int:id>',views.company_show,name = "userprofile"),
    path('companyshow/<int:id>',views.company_showw,name = "company_showw"),
    path('yetenek/',views.programlama_di,name="yetenek"),
    path('yetenekekle/',views.yetenek_olusturma,name="yetenekekle"),
    path('yeteneksil/',views.yetenek_sil,name = "yeteneksil"),
    path('favuserekle/',views.fav_user_ekle,name = "fav_user_ekle"),
    path('favusersil/',views.fav_user_sil,name = "fav_user_sil"),
    path('favilanekle/',views.fav_ilan_ekle,name = "fav_ilan_ekle"),
    path('favilansil/',views.fav_ilan_sil,name = "fav_ilan_sil"),
    path('favorilerim/',views.favorilerim,name = "favorilerim"),
    path('degerlendirme_sil/<int:id>',views.degerlendirme_sil,name = "degerlendirme_sil"),
]
