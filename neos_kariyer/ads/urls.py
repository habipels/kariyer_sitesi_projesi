from django.contrib import admin
from django.urls import path
from . import views

app_name = "ads"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addads/',views.addads,name = "add_ads"),
    path('adsupdate/<int:id>',views.updateads,name = "ads_update"),
    path('adsdelete/<int:id>',views.ads_delete,name = "ads_delete"),
    path('views/<int:id>',views.ads_views_offer,name = "ads_views_offer"),
]
