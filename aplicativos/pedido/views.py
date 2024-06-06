from django.shortcuts import render, get_object_or_404, redirect
from aplicativos.cardapio.models import Prato, Bebida
from aplicativos.mesas.models import Mesa

              
def index(request):
        return render(request, 'index.html')

def pedido(request, mesa_id):
        pratos = Prato.objects.all()
        bebidas = Bebida.objects.all()
        mesa = Mesa.objects.get(id=mesa_id)
        return render(request, 'pedido.html', {"pratos": pratos, "bebidas": bebidas, "mesas": mesa}, )

def imagem_prato(request, prato_id, mesa_id):
        mesa = Mesa.objects.get(id=mesa_id)
        pratos = Prato.objects.get(id=prato_id)
        return render(request, 'imagem.html', {"pratos": pratos, "mesas": mesa})

def imagem_bebida(request, bebida_id, mesa_id):
        mesa = Mesa.objects.get(id=mesa_id)
        bebidas = Bebida.objects.get(id=bebida_id)
        return render(request, 'imagem.html', {"bebidas": bebidas, "mesa": mesa})

def adicionar_prato_a_comanda(request, prato_id, mesa_id):
        prato = Prato.objects.get(id=prato_id)
        Mesa.comanda.update({'nome': prato.nome})
        return redirect('mesa_numero', mesa_id)

def adicionar_bebida_a_comanda(request, bebida_id, mesa_id):
        bebida = Bebida.objects.get(id=bebida_id)
        Mesa.comanda.update({'nome': bebida.nome})
        return redirect('mesa_numero', mesa_id)