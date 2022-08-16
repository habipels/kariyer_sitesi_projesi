from django.contrib import admin
from .models import *
# Register your models here.
class user_table(admin.ModelAdmin):
    list_display = ("user", "isim_soyisim", "email","telefon","user_kategori","lokasyon","kullanici_tipi","create_at")
    list_filter = [
         "isim_soyisim",
         "user_kategori",
         "lokasyon"
         ,"create_at"
    ]
    search_fields = (
        "acceptance_status",
        "kullanici_tipi","lokasyon","create_at"
    )
class company_table(admin.ModelAdmin):
    list_display = ("user", "company_name", "company_email","company_telefon","user_kategori","company_foundation_year","create_at")
    list_filter = [
         "company_name",
         "user_kategori",
         
         "create_at"
    ]
    search_fields = (
        "company_name",
        "user_kategori""create_at"
    )
class user_resume(admin.ModelAdmin):
    list_display = ("baslik", "tarih")
    list_filter = [
          "baslik", "tarih"
    ]
    search_fields = (
        "baslik", "tarih"
    )
class user_yetenek(admin.ModelAdmin):
    list_display = ("user","yetenek_dil", "yetenek_dil")
    list_filter = [
          "yetenek_dil", "yetenek_dil"
    ]
    search_fields = (
        "yetenek_dil", "yetenek_dil"
    )
class user_yetenek(admin.ModelAdmin):
    list_display = ("user","yetenek_dil", "yetenek_dil")
    list_filter = [
          "yetenek_dil", "yetenek_dil"
    ]
    search_fields = (
        "yetenek_dil", "yetenek_dil"
    )
class user_calisma(admin.ModelAdmin):
    list_display = ("user","is_b", "calisma_durumu","deneyim","calisma")
    list_filter = [
          "is_b", "calisma_durumu","deneyim","calisma"
    ]
    search_fields = (
        "is_b", "calisma_durumu","deneyim","calisma"
    )
class user_profilac(admin.ModelAdmin):
    list_display = ("user","user")
admin.site.register(degerlendirme)
admin.site.register(dogrulama)
admin.site.register(mail_dogrulama)
admin.site.register(tel_dogrulama)
admin.site.register(fav_user)
admin.site.register(fav_adds)
admin.site.register(user_profil,user_table)
admin.site.register(resume,user_resume)
admin.site.register(working_condition,user_calisma)
admin.site.register(abilities,user_yetenek)
admin.site.register(company_profile,company_table)
admin.site.register(profil_acma,user_profilac)