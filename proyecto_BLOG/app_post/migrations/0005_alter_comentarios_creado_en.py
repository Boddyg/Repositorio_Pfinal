# Generated by Django 4.1.4 on 2022-12-20 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_post', '0004_comentarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='creado_en',
            field=models.DateField(auto_now_add=True),
        ),
    ]
