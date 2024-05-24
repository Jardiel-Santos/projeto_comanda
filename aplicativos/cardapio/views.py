from django.shortcuts import render
from aplicativos.cardapio.models import Prato, Bebida


def index(request):
        return render(request, 'index.html')

def cardapio(request):
        pratos = Prato.objects.all()
        bebidas = Bebida.objects.all()
        return render(request, 'cardapio.html', {"pratos": pratos, "bebidas": bebidas})
               