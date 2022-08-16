from django.contrib import admin
from .models import *
# Register your models here.


class ilanlar(admin.ModelAdmin):
    list_display = ("ilan_sahibi", "ilan_basligi", "ilan_olusturma_tarihi")
    list_filter = [
         "ilan_sahibi",
         "ilan_basligi",
         "ilan_olusturma_tarihi"
    ]
    search_fields = (
        "ilan_olusturma_tarihi",
        "ilan_sahibi",
    )
    

admin.site.register(ads_data, ilanlar)
class ilanlar_kategorisi(admin.ModelAdmin):
    list_display = ("ilan", "aranan_deneyim", "lokasyon","ilan_calima_saati","ilan_ucretlendirmesi")
    list_filter = [
         "lokasyon",
         "ilan",
         "aranan_deneyim"
         ,"ilan_calima_saati","ilan_ucretlendirmesi"
    ]
    search_fields = (
        "aranan_deneyim",
        "lokasyon","ilan_calima_saati","ilan_ucretlendirmesi"
    )
    
admin.site.register(category_ads,ilanlar_kategorisi)