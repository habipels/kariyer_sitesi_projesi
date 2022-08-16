"""from django.contrib import admin
from django.urls import path
from .views import *

app_name = "pay"

urlpatterns = [
    path('buy/', index, name='indexx'),
    path('payment/<int:id>', payment, name='payment'),
    path('result/', result, name='result'),
    path('success/', success, name='success'),
    path('failure/', fail, name='failure'),
]
"""