from django.contrib import admin
from django.urls import path, include
from aplicativos.pedido.views import index, pedido, imagem

urlpatterns = [
    path('',index),
    path('pedido', pedido, name= 'pedido'),
    path('imagem/<int:prato_id>', imagem, name= 'imagem'),
]

