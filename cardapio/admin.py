from django.contrib import admin
from cardapio.models import Prato

class ListandoPratos(admin.ModelAdmin):
    list_display = ("nome", "descrição", "fotografia", "categoria")




admin.site.register(Prato, ListandoPratos)