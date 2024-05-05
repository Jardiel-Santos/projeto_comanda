from django.db import models

class Prato(models.Model):
    OPCOES_CATEGORIAS = [
        ("LANCHE", "Lanche"),
        ("PIZZA", "Pizza"),
        ("HOTDOG", "Hotdog")
    ]

    nome = models.CharField(max_length=50, null= False, blank= False)
    descrição = models.CharField(max_length=100, null= False, blank= False)
    fotografia = models.ImageField(upload_to="fotos_pratos", blank= False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIAS, default='')