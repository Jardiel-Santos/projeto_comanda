from django.contrib import admin
from aplicativos.funcionarios.models import Funcionario

class ListandoGarcons(admin.ModelAdmin):
    list_display = ("nome", "descricao", "categoria")
    search_fields= ("nome", "categoria")
    list_per_page = 10

class ListandoCozinheiros(admin.ModelAdmin):
    list_display = ("nome", "descricao", "categoria")
    search_fields= ("nome", "categoria")
    list_per_page = 10

class ListandoCaixas(admin.ModelAdmin):
    list_display = ("nome", "descricao", "categoria")
    search_fields= ("nome", "categoria")
    list_per_page = 10


admin.site.register(Funcionario)

