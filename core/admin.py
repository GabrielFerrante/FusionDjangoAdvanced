from django.contrib import admin

# Register your models here.
from .models import Cargo, Servico, Funcionario,Feature

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'ativo','criado','modificado' ]

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['servico', 'icone', 'ativo', 'modificado']

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    #Como na Model do Cargo definimos no __str__ que o objeto se apresenta com o nome
    #Irá retornar o nome dele no admin o cargo
    list_display = ['nome', 'cargo','modificado', 'ativo']

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['titulo','icone','descricao']