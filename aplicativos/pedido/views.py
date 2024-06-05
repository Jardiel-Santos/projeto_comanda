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

def imagem_bebida(request, bebida_id):
        bebidas = get_object_or_404(Bebida, pk=bebida_id)
        return render(request, 'imagem.html', {"bebidas": bebidas})

def adicionar_a_comanda(request,prato_id, mesa_id):
        prato = Prato.objects.get(id=prato_id)
        numero = 0
        Mesa.comanda.update({'nome': prato.nome})
        return redirect('mesa_numero', mesa_id)
