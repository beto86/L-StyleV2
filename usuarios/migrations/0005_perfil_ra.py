# Generated by Django 3.2.4 on 2021-08-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_pais_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='ra',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='RA'),
        ),
    ]
