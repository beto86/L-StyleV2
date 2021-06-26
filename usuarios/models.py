from django.db import models
from django.contrib.auth.models import User
from cadastros.models import Endereco

# Create your models here.


class Perfil(models.Model):
    sexo_choice = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('Prefiro_nao_opinar', 'Prefiro não opinar'),
    )
    nome_completo = models.CharField(
        max_length=50, null=True, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=14, null=True, verbose_name='CPF')
    telefone = models.CharField(max_length=16, null=True)
    sexo = models.CharField(max_length=30, choices=sexo_choice, null=True)
    data_nascimento = models.DateField(
        blank=True, null=True, verbose_name='Data de Nascimento')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, related_name='enderecos',
                                 on_delete=models.CASCADE, null=True, verbose_name='Endereço')
    criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criação')
    atualizacao = models.DateTimeField(
        auto_now=True, verbose_name='Atualização')

    class Meta:
        verbose_name = 'Perfil'

    def __str__(self):
        return self.cpf
