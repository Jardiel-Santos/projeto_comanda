from django.contrib import admin
from django.urls import path, include
from cardapio.views import index

urlpatterns = [
    path('',index),
]


    
    
