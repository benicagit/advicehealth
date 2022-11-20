from django.contrib import admin
from .models import Veiculo, Proprietario


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'cor', 'tipo', 'proprietario')


@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf')

