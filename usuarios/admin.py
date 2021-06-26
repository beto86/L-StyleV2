from django.contrib import admin
from .models import Perfil

# Register your models here.


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'cpf', 'telefone', 'sexo',
                    'data_nascimento', 'usuario', 'endereco', 'criacao', 'atualizacao')
