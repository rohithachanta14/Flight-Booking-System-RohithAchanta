from django.urls import path
from Flights import views
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns=[
path('',views.base,name='base'),
path('about/',views.about,name='about'),
path('signup/',views.registerPage,name='registerPage'),
path('signin/',views.loginPage,name='loginPage'),
path('logout/',views.logOutUser,name='logout'),
path('home/',views.home,name='home'),
path('available/',views.available,name='available'),


]
