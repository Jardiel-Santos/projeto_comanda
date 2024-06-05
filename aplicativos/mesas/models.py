from django.db import models
from aplicativos.cardapio.models import Prato



class Mesa(models.Model):
    numero = models.CharField(max_length=2, null=False, blank=False)
    lugares = models.CharField(max_length=2, null=False, blank=False)
    disponivel = models.BooleanField(default=True, null=False, blank=False)
    comanda = {}

    def __str__(self):
        return self.numero