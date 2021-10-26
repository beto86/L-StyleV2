from django.contrib import admin
from .models import Perfil, Cidade, Estado, Pais, UsuarioTurma

# Register your models here.


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'ra', 'cpf', 'telefone', 'sexo',
                    'data_nascimento', 'usuario', 'endereco', 'numero',
                    'cep', 'cidade', 'estado', 'pais', 'criacao', 'atualizacao', 'usuarioTurma')


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'uf', 'ibge')


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'uf', 'ibge', 'pais', 'ddd')


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nome_pt', 'sigla', 'bacen')


@admin.register(UsuarioTurma)
class UsuarioTurma(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'turma')
