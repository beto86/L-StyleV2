# Generated by Django 3.2.4 on 2021-06-20 13:20
# criação do banco de dados

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=45, verbose_name='CEP')),
                ('rua', models.CharField(max_length=45)),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('complemento', models.CharField(
                    blank=True, max_length=45, null=True)),
                ('bairro', models.CharField(max_length=45)),
                ('cidade', models.CharField(max_length=45)),
                ('estado', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Endereço',
            },
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(
                    max_length=300, verbose_name='Descrição')),
                ('recomendacao', models.TextField(
                    max_length=300, verbose_name='Recomendação')),
            ],
            options={
                'verbose_name': 'Estilo',
            },
        ),
        migrations.CreateModel(
            name='FormaAprendizagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(
                    max_length=300, verbose_name='Descrição')),
                ('recomendacao', models.TextField(
                    max_length=300, verbose_name='Recomendação')),
            ],
            options={
                'verbose_name': 'Estilo',
            },
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                 related_name='instituicao_enderecos', to='cadastros.endereco', verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Instituição de Ensino',
            },
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(
                    max_length=100, verbose_name='Descrição')),
                ('ordem', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Opção',
            },
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(
                    max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Questão',
            },
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(
                    max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Questionário',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('ra', models.CharField(max_length=10, unique=True, verbose_name='RA')),
                ('periodo', models.IntegerField(verbose_name='Período')),
                ('ano', models.IntegerField()),
                ('curso', models.CharField(max_length=45)),
                ('turno', models.CharField(blank=True, max_length=15, null=True)),
                ('instituicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                 related_name='instituicao_ensinos', to='cadastros.instituicao', verbose_name='Instituição de Ensino')),
            ],
            options={
                'verbose_name': 'Turma',
            },
        ),
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(
                    max_length=100, verbose_name='Descriçãos')),
                ('data', models.DateField(auto_now_add=True)),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('chave_acesso', models.CharField(blank=True,
                 max_length=30, null=True, verbose_name='Chave de Acesso')),
                ('ativo', models.BooleanField(default=False)),
                ('professor', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='questionarios', to='cadastros.questionario')),
                ('turma', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.CASCADE, related_name='turmas', to='cadastros.turma')),
            ],
            options={
                'verbose_name': 'Teste',
            },
        ),
        migrations.CreateModel(
            name='Tentativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('concluiu', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                 related_name='tentativa_alunos', to=settings.AUTH_USER_MODEL)),
                ('teste', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                 related_name='testes', to='cadastros.teste')),
            ],
            options={
                'verbose_name': 'Tentativa',
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('aluno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                 related_name='alunos', to=settings.AUTH_USER_MODEL)),
                ('opcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='opcaos', to='cadastros.opcao', verbose_name='Opção')),
                ('tentativa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                 to='cadastros.tentativa', verbose_name='tentativas')),
            ],
            options={
                'verbose_name': 'Resposta',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), (
                    'Prefiro_nao_opinar', 'Prefiro não opinar')], default='Prefiro_nao_opinar', max_length=30, null=True)),
                ('data_nascimento', models.DateField(blank=True,
                 null=True, verbose_name='Data de Nascimento')),
                ('fone', models.CharField(blank=True, max_length=12,
                 null=True, verbose_name='Telefone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cpf', models.CharField(blank=True,
                 max_length=12, null=True, verbose_name='CPF')),
                ('criacao', models.DateTimeField(
                    auto_now_add=True, verbose_name='Criação')),
                ('atualizacao', models.DateTimeField(
                    auto_now=True, verbose_name='Atualização')),
                ('endereco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                 related_name='enderecos', to='cadastros.endereco', verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Perfil',
            },
        ),
        migrations.AddField(
            model_name='opcao',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='questaos', to='cadastros.questao', verbose_name='Questão'),
        ),
        migrations.AlterUniqueTogether(
            name='opcao',
            unique_together={('descricao', 'questao')},
        ),
    ]
