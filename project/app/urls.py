from django.contrib import admin
from django.urls import path
from.views import home
from.views import about
from.views import contact




urlpatterns=[
    
    path('home/',home,name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact')
]