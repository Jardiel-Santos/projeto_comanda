from django.contrib import admin
from cardapio.models import Prato, Bebida

class ListandoPratos(admin.ModelAdmin):
    list_display = ("nome", "descrição", "fotografia", "categoria")


class ListandoBebidas(admin.ModelAdmin):
    list_display = ("nome", "descrição", "fotografia", "categoria")




admin.site.register(Prato, ListandoPratos)
admin.site.register(Bebida, ListandoBebidas)