from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Endereco(models.Model):
    cep = models.CharField(max_length=45, verbose_name='CEP')
    rua = models.CharField(max_length=45)
    numero = models.IntegerField(verbose_name='Número')
    complemento = models.CharField(max_length=45, blank=True, null=True)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Endereço'

    def __str__(self):
        return f'{self.rua}, {self.numero}, {self.cidade}'


class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, related_name='%(class)s_enderecos',
                                 on_delete=models.CASCADE, blank=True, null=True, verbose_name='Endereço')

    class Meta:
        verbose_name = 'Instituição de Ensino'

    def __str__(self):
        return self.nome


class Turma(models.Model):
    turno_choice = (
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Noturno', 'Noturno'),
    )
    nome = models.CharField(max_length=45)
    ra = models.CharField(max_length=10, unique=True, verbose_name='RA')
    periodo = models.IntegerField(verbose_name='Período')
    ano = models.IntegerField()
    curso = models.CharField(max_length=45)
    turno = models.CharField(
        max_length=15, choices=turno_choice, blank=True, null=True)
    instituicao = models.ForeignKey(
        Instituicao, related_name='instituicao_ensinos', on_delete=models.CASCADE, verbose_name='Instituição de Ensino', blank=True, null=True)

    class Meta:
        verbose_name = 'Turma'

    def __str__(self):
        return self.nome
