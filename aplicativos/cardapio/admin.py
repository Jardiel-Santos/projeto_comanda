from django.contrib import admin
from aplicativos.cardapio.models import Prato, Bebida

class ListandoPratos(admin.ModelAdmin):
    list_display = ("nome", "descricao", "foto", "categoria")
    search_fields= ("nome", "categoria")
    list_per_page = 10


class ListandoBebidas(admin.ModelAdmin):
    list_display = ("nome", "descricao", "foto", "categoria")
    search_fields= ("nome", "categoria")
    list_per_page = 10




admin.site.register(Prato, ListandoPratos)
admin.site.register(Bebida, ListandoBebidas)