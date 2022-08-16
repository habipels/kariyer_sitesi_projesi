from django.contrib import admin
from .models import *
# Register your models here.
class user_status_if(admin.ModelAdmin):
    list_display = ("user","durum")
    list_filter = [
          "durum"
    ]
    search_fields = (
        "durum",
    )
admin.site.register(user_status,user_status_if)