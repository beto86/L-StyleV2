# Generated by Django 3.2.4 on 2021-07-09 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20210626_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('nome_pt', models.CharField(max_length=60, verbose_name='nome')),
                ('sigla', models.CharField(max_length=3)),
                ('bacen', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='cep',
            field=models.CharField(max_length=45, null=True, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='numero',
            field=models.CharField(max_length=10, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='endereco',
            field=models.CharField(max_length=100, null=True, verbose_name='Endereço'),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('ibge', models.IntegerField()),
                ('ddd', models.CharField(max_length=30)),
                ('pais', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('ibge', models.IntegerField()),
                ('uf', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.estado')),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.cidade'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.estado'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='pais',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.pais', verbose_name='País'),
        ),
    ]
