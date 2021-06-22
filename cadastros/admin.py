from django.contrib import admin
from .models import Endereco, Estilo, FormaAprendizagem, Instituicao, Opcao, Perfil, Questao, Questionario, Resposta, Tentativa, Teste, Turma

# Register your models here.
"""
admin.site.register(Endereco)
admin.site.register(Estilo)
admin.site.register(FormaAprendizagem)
admin.site.register(Instituicao)
admin.site.register(Opcao)
admin.site.register(Perfil)
admin.site.register(Questao)
admin.site.register(Questionario)
admin.site.register(Resposta)
admin.site.register(Tentativa)
admin.site.register(Teste)
admin.site.register(Turma)
"""


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cep', 'rua', 'numero', 'complemento',
                    'bairro', 'cidade', 'estado')


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'sexo', 'data_nascimento', 'cpf',
                    'fone', 'endereco', 'criacao', 'atualizacao')


@admin.register(Instituicao)
class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco')


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ra', 'periodo', 'ano',
                    'curso', 'turno', 'instituicao')


@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')


@admin.register(Teste)
class TesteAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'professor', 'questionario',
                    'turma', 'data', 'hora', 'chave_acesso', 'ativo')


@admin.register(Tentativa)
class TentativaAdmin(admin.ModelAdmin):
    list_display = ('id', 'teste', 'aluno', 'data', 'concluiu')


@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao')


@admin.register(Opcao)
class OpcaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'questao', 'descricao', 'ordem')


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tentativa', 'opcao', 'valor', 'aluno')


@admin.register(Estilo)
class EstiloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'recomendacao')


@admin.register(FormaAprendizagem)
class FormaAprendizagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'recomendacao')
