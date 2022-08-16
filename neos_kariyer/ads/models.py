from django.db import models
from ckeditor.fields import RichTextField
from all_category.models import *
# Create your models here.


class ads_data(models.Model):
    ilan_sahibi = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "İlan Sahibi ")
    ilan_basligi = models.CharField(max_length = 50,verbose_name = "İlan")
    kisa_ilan_aciklamasi = models.TextField(max_length = 250,verbose_name = "Kısa İlan Açıklaması")
    ilan = RichTextField()
    ilan_olusturma_tarihi = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    İlan_gorseli = models.FileField(upload_to='ilan_gorsel/',blank = True,null = True,verbose_name="ilana Fotoğraf Ekleyin")
    ilan_gecis_tablosu = models.DateTimeField(null = True,verbose_name="İlan Kalma Tarihi")
    chip_amunt = models.IntegerField(null=True)
    offer_much = models.IntegerField(null=True)
    def __str__(self):
        return self.ilan_basligi

    class Meta:
        ordering = ['-ilan_olusturma_tarihi']

class category_ads(models.Model):
    ilan = models.ForeignKey(ads_data,on_delete = models.CASCADE,verbose_name = "İlan Sahibi ")
    aranan_deneyim = models.ForeignKey(deneyim,null=True,on_delete = models.CASCADE,verbose_name = "İlan Deneyimi ")
    lokasyon = models.ForeignKey(lokasyon,null=True,on_delete = models.CASCADE,verbose_name = "İlan Lokasyonu ")
    ilan_calima_saati = models.ForeignKey(kategoriler,null=True,on_delete = models.CASCADE,verbose_name = "İlan Çalışma Saati ")
    ilan_ucretlendirmesi = models.ForeignKey(ucretlendirme,on_delete = models.CASCADE,verbose_name = "İlan Ücretlendirmesi")