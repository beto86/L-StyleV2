# Generated by Django 3.2.4 on 2021-10-10 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuarios', '0005_perfil_ra'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cep',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.cidade'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.estado'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.pais', verbose_name='País'),
        ),
    ]
