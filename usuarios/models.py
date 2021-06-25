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
    nome_cmpleto = models.CharField(
        max_length=50, null=True, verbose_name='Nome Completo')
    cpf = models.CharField(max_length=14, null=True, verbose_name='CPF')
    # mudar max_length para 16
    telefone = models.CharField(max_length=12, null=True)
    sexo = models.CharField(max_length=30, choices=sexo_choice,
                            default='Prefiro_nao_opinar', blank=True, null=True)
    data_nascimento = models.DateField(
        blank=True, null=True, verbose_name='Data de Nascimento')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, related_name='enderecos',
                                 on_delete=models.CASCADE, blank=True, null=True, verbose_name='Endereço')
    criacao = models.DateTimeField(auto_now_add=True, verbose_name='Criação')
    atualizacao = models.DateTimeField(
        auto_now=True, verbose_name='Atualização')

    class Meta:
        verbose_name = 'Perfil'

    def __str__(self):
        return self.cpf
