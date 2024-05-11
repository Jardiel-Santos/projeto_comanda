from django.contrib import admin
from django.urls import path, include
from cardapio.views import index, cardapio

urlpatterns = [
    path('',index),
    path('cardapio', cardapio, name= 'cardapio'),
]


    
    
