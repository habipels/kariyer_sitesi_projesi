from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# kullanıcıların şirketmi yoksa freelancermi olduğunu belirler.
class user_status(models.Model):
    user = models.OneToOneField(User,null=True,on_delete = models.CASCADE,verbose_name="Kullanıcı Durumu")
    durum = models.BooleanField(null=True)

class parola_sifirla(models.Model):
    user = models.OneToOneField(User,null=True,on_delete = models.CASCADE,verbose_name="Kullanıcı Durumu")
    sifirla = models.IntegerField()