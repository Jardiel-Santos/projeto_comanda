from django.db import models

class Prato(models.Model):
    OPCOES_CATEGORIAS_PRATOS = [
        ("LANCHE", "Lanche"),
        ("PIZZA", "Pizza"),
        ("HOTDOG", "Hotdog")
    ]

    nome = models.CharField(max_length=50, null= False, blank= False)
    descricao = models.CharField(max_length=100, null= False, blank= False)
    fotografia = models.ImageField(upload_to="media/fotos_pratos", blank= False)
    categoria = models.CharField(max_length=20, choices=OPCOES_CATEGORIAS_PRATOS, default='')

    def delete(self, *args, **kwargs):
        self.fotografia.delete(save=False)
        super().delete(*args, **kwargs)
        
    def __str__(self):
        return self.nome

class Bebida(models.Model):
    OPCOES_CATEGORIAS_BEBIDAS = [
        ("REFRIGERANTES", "Refrigerantes"),
        ("ALCOOLICAS", "Alcoolicas"),
    ]

    nome = models.CharField(max_length=50, null= False, blank= False)
    descricao = models.CharField(max_length=100, null= False, blank= False)
    fotografia = models.ImageField(upload_to="media/fotos_bebidas", blank= False)
    categoria = models.CharField(max_length=20, choices=OPCOES_CATEGORIAS_BEBIDAS, default='')
    
    def delete(self, *args, **kwargs):
        self.fotografia.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nome