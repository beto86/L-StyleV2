# Generated by Django 3.2.4 on 2021-06-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KolbStyleTeste', '0002_auto_20210628_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='opcao',
            name='imagem',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='opcao',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
