from django.db import models
from ads.models import *
# Create your models here.
from django.contrib.auth.models import User
from profil.models import company_profile ,user_profil
class ad_offer_user(models.Model):
    offer_user = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "İlan Teklifi Yapan ")
    ads_ofer = models.ForeignKey(ads_data,on_delete = models.CASCADE,verbose_name = "Teklif Alan İlan ")
    offer_amount = models.IntegerField()
    acceptance_status =models.BooleanField(verbose_name="Kabul Durumu ")
    read_status =models.BooleanField(verbose_name="okundu Durumu ")
    veto_status = models.BooleanField(verbose_name="Red Durumu",null=True)
    offer_date = models.DateField(null=True,auto_now_add=True)


class expert(models.Model):
    expert_offers_user = models.ForeignKey(User ,on_delete = models.CASCADE,verbose_name = "Teklif Alan Kullancıı ")
    offer_user = models.ForeignKey(company_profile,null=True,on_delete = models.CASCADE,verbose_name = "Teklifi Yapan Kullanıcı")
    offer_amount = models.IntegerField(verbose_name="Teklif Edilen Miktar")
    acceptance_status = models.BooleanField(verbose_name="Kabul Durumu ")
    read_status = models.BooleanField(verbose_name="okundu Durumu ")
    veto_status = models.BooleanField(verbose_name="Red Durumu",null=True)
    offer_date = models.DateField(null=True,auto_now_add=True)

class expert_expert(models.Model):
    expert_offers_user = models.ForeignKey(User ,on_delete = models.CASCADE,verbose_name = "Teklif Alan Kullancıı ")
    offer_user = models.ForeignKey(user_profil,null=True,on_delete = models.CASCADE,verbose_name = "Teklifi Yapan Kullanıcı")
    offer_amount = models.IntegerField(verbose_name="Teklif Edilen Miktar")
    acceptance_status = models.BooleanField(verbose_name="Kabul Durumu ")
    read_status = models.BooleanField(verbose_name="okundu Durumu ")
    veto_status = models.BooleanField(verbose_name="Red Durumu",null=True)
    offer_date = models.DateField(null=True,auto_now_add=True)

class teklif_redd(models.Model):
    adds_offer  = models.ForeignKey(ad_offer_user,on_delete = models.CASCADE,verbose_name = "Teklif Alan İlan ")
    redd =models.CharField(max_length=150,verbose_name= "Reddedilme Sebebi")


class call_offer_user_add(models.Model):
    offer_user = models.ForeignKey(user_profil,on_delete = models.CASCADE,verbose_name = "İlan Teklifi Yapan ")
    ads_ofer = models.ForeignKey(ads_data,on_delete = models.CASCADE,verbose_name = "Teklif Alan İlan ")
    acceptance_status =models.BooleanField(verbose_name="Kabul Durumu ")
    read_status =models.BooleanField(verbose_name="okundu Durumu ")
    veto_status = models.BooleanField(verbose_name="Red Durumu",null=True)
    offer_date = models.DateField(null=True,auto_now_add=True)