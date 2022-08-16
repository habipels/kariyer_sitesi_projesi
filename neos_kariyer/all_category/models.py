from django.db import models

# Create your models here.
class kategory_link_ayari(models.CharField):
    def __init__(self, *args, **kwargs):
        super(kategory_link_ayari, self).__init__(*args, **kwargs)
    def get_prep_value(self, value):
        return str(value).lower().replace(" ","_")

class user_adi(models.CharField):
    def __init__(self, *args, **kwargs):
        super(user_adi, self).__init__(*args, **kwargs)
    def get_prep_value(self, value):
        return str(value).upper()
class kategoriler(models.Model):
    kategory_ismi = user_adi(verbose_name="Kategori İsmi",max_length=100)
    ust_kategory = models.ForeignKey("self",blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    link = kategory_link_ayari(max_length=200)
    keywords = models.CharField(max_length=255) 
    
    def __str__(self):
        full_path = [self.kategory_ismi]                  # post.  use __unicode__ in place of
        k = self.ust_kategory
        while k is not None:
            full_path.append(k.ust_kategory)
            
        return ' --> '.join(full_path[::-1])


class sehir_duzeltme(models.CharField):
    def __init__(self, *args, **kwargs):
        super(sehir_duzeltme, self).__init__(*args, **kwargs)
    def get_prep_value(self, value):
        return str(value).upper()
class lokasyon(models.Model):
    sehir_ismi = sehir_duzeltme(verbose_name="Şehir İsmi",max_length=100)
    def __str__(self) :
        return self.sehir_ismi


class programlama_dili(models.Model):
    dil = sehir_duzeltme(verbose_name="Yetenek",max_length=100)
    def __str__(self) :
        return self.dil
class deneyim(models.Model):
    tecrube = models.CharField(verbose_name="Tecrübeler",max_length=20)
    siralama_puani = models.IntegerField(null=True)
    def __str__(self) :
        return self.tecrube

class is_beklentisi(models.Model):
    calisma_beklentisi = models.CharField(verbose_name="İş Beklentisi",max_length=100)
    def __str__(self) :
        return self.calisma_beklentisi
class ucretlendirme(models.Model):
    ucretlendirmesi = models.CharField(verbose_name="İş ücretlenmesi",max_length=100)
    def __str__(self) :
        return self.ucretlendirmesi
class ekip_durumu(models.Model):
    ekip = models.CharField(verbose_name="Ekip Durumu",max_length=100)
    def __str__(self) :
        return self.ekip
class calisma_saati(models.Model):
    calisma_saat = models.CharField(verbose_name="Haftalık çalışma saati",max_length=100)
    def __str__(self) :
        return self.calisma_saat

class current_situation(models.Model):
    calisma_durumu = models.CharField(verbose_name="Çalışma Durumu",max_length=100)
    def __str__(self) :
        return self.calisma_durumu