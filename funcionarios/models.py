from django.db import models

class Funcionario(models.Model):
    OPCOES_CATEGORIAS_FUNCIONARIOS = [
        ("GARCOM", "garcom"),
        ("COZINHEIRO", "cozinheiro"),
        ("CAIXA", "caixa")
    ]

    nome = models.CharField(max_length=50, null= False, blank= False)
    descricao = models.CharField(max_length=100, null= False, blank= False)
    categoria = models.CharField(max_length=20, choices=OPCOES_CATEGORIAS_FUNCIONARIOS, default='')

    def __str__(self):
        return self.nome
