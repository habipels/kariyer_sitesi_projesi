"""from django.shortcuts import render,redirect
import iyzipay
import json
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import requests
from django.contrib import messages
import pprint
from .models import paketler
from profil.models import *
from user_operations.models import user_status
api_key = 'sandbox-nhJQYCPyAV24s4jzzXG6pI31n3SfyBHB'
secret_key = 'sandbox-VMPdBdwIXUTjLtsMms3fN4nKuxtFuG5u'
base_url = 'sandbox-api.iyzipay.com'


options = {
    'api_key': api_key,
    'secret_key': secret_key,
    'base_url': base_url
}
sozlukToken = list()
alacagi_bakiye = list()
prof_id = list()

def index(request):
    context = dict()

    context={"paketler":paketler.objects.all()}
    

    template = 'pay_temp/buy_temp.html'
    return render(request, template, context)


def payment(request,id):
    user_tablosu = user_profil.objects.filter(user=request.user)
    for idiler in user_tablosu:
        prof_id.append(idiler.id)
    z = paketler.objects.filter(id = id)
    for i in z:
        m = i.ilana_alinacak_ucret
        alacagi_bakiye.append(i.teklife_verilecek_ucret)
    context = dict()

    buyer={
        'id': 'BY789',
        'name': 'John',
        'surname': 'Doe',
        'gsmNumber': '+905350000000',
        'email': 'email@email.com',
        'identityNumber': '74300864791',
        'lastLoginDate': '2015-10-05 12:43:35',
        'registrationDate': '2013-04-21 15:12:09',
        'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'ip': '85.34.78.112',
        'city': 'Istanbul',
        'country': 'Turkey',
        'zipCode': '34732'
    }

    address={
        'contactName': 'Jane Doe',
        'city': 'Istanbul',
        'country': 'Turkey',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'zipCode': '34732'
    }

    basket_items=[
        {
            'id': 'BI101',
            'name': 'Binocular',
            'category1': 'Collectibles',
            'category2': 'Accessories',
            'itemType': 'PHYSICAL',
            'price': '0.3'
        },
        {
            'id': 'BI102',
            'name': 'Game code',
            'category1': 'Game',
            'category2': 'Online Game Items',
            'itemType': 'VIRTUAL',
            'price': '0.5'
        },
        {
            'id': 'BI103',
            'name': 'Usb',
            'category1': 'Electronics',
            'category2': 'Usb / Cable',
            'itemType': 'PHYSICAL',
            'price': '0.2'
        }
    ]

    request={
        'locale': 'tr',
        'conversationId': str(prof_id[0]),
        'price': '1',
        'paidPrice': m,
        'currency': 'TRY',
        'basketId': 'B67832',
        'paymentGroup': 'PRODUCT',
        "callbackUrl": "http://localhost:8000/buy/result/",
        "enabledInstallments": ['2', '3', '6', '9'],
        'buyer': buyer,
        'shippingAddress': address,
        'billingAddress': address,
        'basketItems': basket_items,
        # 'debitCardAllowed': True
    }

    checkout_form_initialize = iyzipay.CheckoutFormInitialize().create(request, options)

    #print(checkout_form_initialize.read().decode('utf-8'))
    page = checkout_form_initialize
    header = {'Content-Type': 'application/json'}
    content = checkout_form_initialize.read().decode('utf-8')
    json_content = json.loads(content)
    print(type(json_content))
    print(json_content["checkoutFormContent"])
    print("************************")
    print(json_content["token"])
    print("************************")
    sozlukToken.append(json_content["token"])
    return HttpResponse(json_content["checkoutFormContent"])



@require_http_methods(['POST'])
@csrf_exempt
def result(request):
    #m = user_profil.objects.filter(user_id = request.user)
    
    context = dict()

    url = request.META.get('indexx')

    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'token': sozlukToken[0]
    }
    checkout_form_result = iyzipay.CheckoutForm().retrieve(request, options)
    print("************************")
    print(type(checkout_form_result))
    result = checkout_form_result.read().decode('utf-8')
    print("************************")
    print(sozlukToken[0])   # Form oluşturulduğunda 
    print("************************")
    print("************************")
    sonuc = json.loads(result, object_pairs_hook=list)
    #print(sonuc[0][1])  # İşlem sonuç Durumu dönüyor
    #print(sonuc[5][1])   # Test ödeme tutarı
    print("************************")
    for i in sonuc:
        print(i)
    print("************************")
    print(sozlukToken)
    print("************************")
    if sonuc[0][1] == 'success':
        fonksiyon(request,sonuc[5][1])
        context['success'] = 'Başarılı İŞLEMLER'
        return redirect("/")

    elif sonuc[0][1] == 'failure':
        context['failure'] = 'Başarısız'
        return HttpResponse("hata")

    return HttpResponse("olmadı")

def fonksiyon(request,k):
    durumm = user_status.objects.filter(user=prof_id[0])
    for i in durumm:
        kontrol = i.durum
    if kontrol:
        z = user_profil.objects.filter(user=prof_id[0])
    else:
        z = company_profile.objects.filter(user=prof_id[0])
    print(type(z))
    print(request)
    for al in z:
        netbakiye = al.bakiye
    topbakiye = netbakiye +alacagi_bakiye[0]
    z.update(bakiye=topbakiye)
    return redirect("/")

def success(request):
    context = dict()
    context['success'] = 'İşlem Başarılı'

    template = 'pay_temp/ok.html'
    return render(request, template, context)


def fail(request):
    context = dict()
    context['fail'] = 'İşlem Başarısız'

    template = 'pay_temp/fail.html'
    return render(request, template, context)
"""