from django.contrib import admin
from django.urls import path
from aplicativos.cardapio.views import index, cardapio

urlpatterns = [
    path('',index),
    path('cardapio', cardapio, name= 'cardapio'),
]


    
    
