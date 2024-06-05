from django.contrib import admin
from django.urls import path, include
from aplicativos.pedido.views import index, pedido, imagem_prato, imagem_bebida, adicionar_a_comanda


urlpatterns = [
    path('',index),
    path('mesas/<int:mesa_id>/pedido', pedido, name= 'pedido'),
    path('mesas/<int:mesa_id>/pedido/imagem/prato/<int:prato_id>', imagem_prato, name= 'imagem_prato'),
    path('pedido/imagem/bebida/<int:bebida_id>', imagem_bebida, name= 'imagem_bebida'),
    path('adicionar_a_comanda/<int:mesa_id>/<int:prato_id>', adicionar_a_comanda, name= 'adicionar_a_comanda'),
]

