from django.shortcuts import render, get_object_or_404
from aplicativos.cardapio.models import Prato, Bebida
              
def index(request):
        return render(request, 'index.html')

def pedido(request):
        pratos = Prato.objects.all()
        bebidas = Bebida.objects.all()
        return render(request, 'pedido.html', {"pratos": pratos, "bebidas": bebidas})

def imagem(request, prato_id):
    pratos = get_object_or_404(Prato, pk=prato_id)
    return render(request, 'imagem.html', {"pratos": pratos})
