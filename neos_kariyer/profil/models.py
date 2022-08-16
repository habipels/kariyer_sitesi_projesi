from django.db import models
from all_category.models import *
# Create your models here.
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
class user_profil(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    isim_soyisim = user_adi(max_length=200 ,null=True,verbose_name="Adı Soyadı")
    email = models.EmailField(max_length=200 ,null=True,verbose_name="E-Posta")
    telefon = models.CharField(max_length=11 ,null=True,verbose_name="Telefon Numarası")
    profil_img = models.FileField(upload_to='profil/',null = True, blank = True ,verbose_name="Profil Görseli" )
    background = models.FileField(upload_to='back/',null = True, blank = True ,verbose_name="Arkaplan Görseli" )
    user_kategori = models.ForeignKey(kategoriler,on_delete = models.CASCADE,null=True, blank=True, help_text="Kullanıcı Biligi Kategorisi")
    on_bilgi = models.TextField(null=True,verbose_name="Kartvizit Bilgisi")
    lokasyon = models.ForeignKey(lokasyon,null=True,on_delete = models.CASCADE,verbose_name="Lokasyon Bilgisi")
    minumum_ucret = models.IntegerField(null=True)
    kullanici_tipi = models.CharField(max_length=1 ,null=True,verbose_name="Kullanıcı Paket Durumu ")
    bakiye = models.IntegerField(null=True)
    create_at = models.DateField(auto_now_add=True,null=True)
    degerlendirme_puanli = models.IntegerField(null=True)
    company_about = RichTextField(null=True)
    
class resume(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    yon = models.CharField(max_length=1,null=True)
    baslik = models.CharField(max_length=40,verbose_name="Başlık")
    aciklama = models.TextField(max_length=150,verbose_name="Açıklama")
    tarih = models.DateField(verbose_name="Tarih")


class working_condition(models.Model):
    user = models.OneToOneField(User,null=True,on_delete = models.CASCADE,verbose_name="Kullanıcı Bilgisi")
    is_b = models.ForeignKey(is_beklentisi,null=True,on_delete = models.CASCADE,verbose_name="İş Beklentisi")
    calisma_durumu = models.ForeignKey(current_situation,null=True,on_delete = models.CASCADE,verbose_name="Çalışma Durumu")
    deneyim = models.ForeignKey(deneyim,null=True,on_delete = models.CASCADE,verbose_name="Deneyim")
    calisma = models.ForeignKey(calisma_saati,null=True,on_delete = models.CASCADE,verbose_name="İş Çalışma Saati")
    

class abilities(models.Model):
    user =models.ForeignKey(User,null=True,on_delete = models.CASCADE,verbose_name="Kullanıcı Bilgisi")
    yetenek_dil = models.ForeignKey(programlama_dili,null=True,on_delete = models.CASCADE,verbose_name="Yetenek Bilgisi")
    deneyimler = models.ForeignKey(deneyim,null=True,on_delete = models.CASCADE,verbose_name="Deneyim Bilgisi")


class company_profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    company_name = user_adi(max_length=200 ,null=True,verbose_name="Şirket Adı")
    company_email = models.EmailField(max_length=22 ,null=True,verbose_name="E-Posta")
    company_telefon = models.CharField(max_length=11 ,null=True,verbose_name="Telefon Numarası")
    profil_img = models.FileField(upload_to='profil/',null = True, blank = True ,verbose_name="Profil Görseli" )
    background = models.FileField(upload_to='back/',null = True, blank = True ,verbose_name="Arkaplan Görseli" )
    user_kategori = models.ForeignKey(kategoriler,on_delete = models.CASCADE,null=True, blank=True, help_text="Kullanıcı Biligi Kategorisi")
    company_explanation = models.TextField(null=True,verbose_name="Şirket Açıklaması")
    lokasyon = models.TextField(null=True,verbose_name="Şirket Lokasyon")
    company_foundation_year = models.DateField(auto_now_add=True,null=True)
    kullanici_tipi = models.CharField(max_length=1 ,null=True,verbose_name="Kullanıcı Paket Durumu ")
    bakiye = models.IntegerField(null=True)
    create_at = models.DateField(auto_now_add=True,null=True)
    company_about = RichTextField(null=True)

class profil_acma(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    profil = models.ForeignKey(user_profil,on_delete = models.CASCADE,null=True)

class degerlendirme(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True,verbose_name="Oy Veren")
    profil = models.ForeignKey(user_profil,on_delete = models.CASCADE,null=True,verbose_name="Oy Alan")
    puan = models.IntegerField()

class dogrulama(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    mail  = models.BooleanField()
    telefon = models.BooleanField()

class mail_dogrulama(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    mail  = models.IntegerField()

class tel_dogrulama(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    telefon  = models.IntegerField()


class fav_user(models.Model):
    expert_offers_user = models.ForeignKey(User ,on_delete = models.CASCADE,verbose_name = "Sahip ")
    offer_user = models.ForeignKey(user_profil,null=True,on_delete = models.CASCADE,verbose_name = "favori user")

from ads.models import *
class fav_adds(models.Model):
    expert_offers_user = models.ForeignKey(User ,on_delete = models.CASCADE,verbose_name = "Sahip ")
    ads_ofer = models.ForeignKey(ads_data,on_delete = models.CASCADE,verbose_name = "Teklif Alan İlan ")
    