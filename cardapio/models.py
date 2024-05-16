from django.db import models
from decimal import Decimal
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

class Prato(models.Model):
    OPCOES_CATEGORIAS_PRATOS = [
        ("LANCHE", "Lanche"),
        ("PIZZA", "Pizza"),
        ("HOTDOG", "Hotdog")
    ]

    nome = models.CharField(max_length=50, null= False, blank= False)
    descricao = models.CharField(max_length=100, null= False, blank= False)
    foto = models.ImageField(upload_to="fotos_pratos", blank= True)
    categoria = models.CharField(max_length=20, choices=OPCOES_CATEGORIAS_PRATOS, default='')
    valor = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal(0))

    """Remove as fotos da pasta media"""
    def delete(self, *args, **kwargs):
        self.foto.delete(save=False)
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
    foto = models.ImageField(upload_to="fotos_bebidas", blank= False)
    categoria = models.CharField(max_length=20, choices=OPCOES_CATEGORIAS_BEBIDAS, default='')
   
    # TESTE DO MONEYFIELD
   
    # valor = MoneyField(
    #     max_digits=5, decimal_places=2, default=0, default_currency='BRL',
    #     validators=[
    #         MinMoneyValidator(Decimal(0.00)), MaxMoneyValidator(Decimal(999.99)),
    #     ]
    # )
    
    """Remove as fotos da pasta media"""
    def delete(self, *args, **kwargs):
        self.foto.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nome
     