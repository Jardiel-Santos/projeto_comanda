from django.shortcuts import render
from aplicativos.mesas.models import Mesa

def index(request):
        return render(request, 'index.html')

def mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas.html', {"mesas": mesas})