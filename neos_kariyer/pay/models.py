from django.db import models

# Create your models here.

class paketler(models.Model):
   
    paket_basligi = models.CharField(max_length = 50,verbose_name = "İlan")
    kisa_ilan_aciklamasi = models.CharField(max_length = 250,verbose_name = "Kısa İlan Açıklaması")
    ilan_olusturma_tarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    İlan_gorseli = models.FileField(upload_to='paket/',blank = True,null = True,verbose_name="ilana Fotoğraf Ekleyin")
    ilana_alinacak_ucret = models.IntegerField(null=True)
    teklife_verilecek_ucret = models.IntegerField(null=True)

class odemeler(models.Model):
    user_payment = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Paket Satın Alan")
    user_payment_much = models.IntegerField()
    user_payment_date = models.DateField(null=True,auto_now_add=True)