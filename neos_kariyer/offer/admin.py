from django.contrib import admin
from .models import *
# Register your models here.
class offer(admin.ModelAdmin):
    list_display = ("offer_user", "ads_ofer", "offer_amount","acceptance_status","read_status","veto_status")
    list_filter = [
         "offer_date",
         "acceptance_status",
         "read_status"
         ,"veto_status"
    ]
    search_fields = (
        "acceptance_status",
        "offer_date","read_status","veto_status"
    )
class offer_uzman(admin.ModelAdmin):
    list_display = ("expert_offers_user", "offer_user", "offer_amount","acceptance_status","read_status","veto_status","offer_date")
    list_filter = [
         "offer_date",
         "acceptance_status",
         "read_status"
         ,"veto_status"
    ]
    search_fields = (
        "acceptance_status",
        "offer_date","read_status","veto_status"
    )
class offer_offer(admin.ModelAdmin):
    list_display = ("expert_offers_user", "offer_user", "offer_amount","acceptance_status","read_status","veto_status","offer_date")
    list_filter = [
         "offer_date",
         "acceptance_status",
         "read_status"
         ,"veto_status"
    ]
    search_fields = (
        "acceptance_status",
        "offer_date","read_status","veto_status"
    )
admin.site.register(ad_offer_user,offer)
admin.site.register(expert,offer_uzman)
admin.site.register(expert_expert,offer_offer)
admin.site.register(teklif_redd)
admin.site.register(call_offer_user_add)