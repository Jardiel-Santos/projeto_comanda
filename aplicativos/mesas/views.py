from django.shortcuts import render, get_object_or_404
from aplicativos.mesas.models import Mesa

def index(request):
        return render(request, 'index.html')

def mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas.html', {"mesas": mesas})

def mesa_id(request, mesa_id):
    mesa_id = get_object_or_404(Mesa, pk=mesa_id)
    return render(request, 'mesa_id.html', {"mesas": mesa_id})