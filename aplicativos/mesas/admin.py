from django.contrib import admin
from aplicativos.mesas.models import Mesa

class ListandoMesas(admin.ModelAdmin):
    list_display = ("numero", "lugares", "disponivel")
    search_fields= ("numero", "disponivel")
    list_per_page = 10

admin.site.register(Mesa, ListandoMesas)
