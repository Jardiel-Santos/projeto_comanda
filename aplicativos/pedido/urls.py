from django.contrib import admin
from django.urls import path
from aplicativos.pedido.views import index, pedido, imagem_prato, imagem_bebida, adicionar_prato_a_comanda, adicionar_bebida_a_comanda, limpar_comanda


urlpatterns = [
    path('',index),
    path('mesas/<int:mesa_id>/pedido', pedido, name= 'pedido'),
    path('mesas/<int:mesa_id>/pedido/imagem/prato/<int:prato_id>', imagem_prato, name= 'imagem_prato'),
    path('mesas/<int:mesa_id>/pedido/imagem/bebida/<int:bebida_id>', imagem_bebida, name= 'imagem_bebida'),
    path('adicionar_prato_a_comanda/<int:mesa_id>/<int:prato_id>', adicionar_prato_a_comanda, name= 'adicionar_prato_a_comanda'),
    path('adicionar_bebida_a_comanda/<int:mesa_id>/<int:bebida_id>', adicionar_bebida_a_comanda, name= 'adicionar_bebida_a_comanda'),
    path('limpar_comanda/<int:mesa_id>', limpar_comanda, name='limpar_comanda'),
]

