from django.contrib import admin
from django.urls import path
from . import views

app_name = "user_operations"

urlpatterns = [
    path('register/',views.user_register,name = "register"),
    path('login/',views.user_login,name = "login"),
    path('logout/',views.user_logout,name = "logout"),
    path('reset/<int:idim>/<int:kod>',views.parola_sifirlama,name = "reset"),
    path('passrest/',views.pass_reset,name="passreset"),
    path('kod/',views.email_gonder,name = "email_gonder"),
    path('membership/<int:id>',views.membership,name = "membership"),

]
