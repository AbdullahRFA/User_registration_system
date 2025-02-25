from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('login/',views.Login,name='login' ),
    path('',views.SignUp,name='signup' ),
    path('home/',views.HomePage,name='homepage' ),
    
]