# Generated by Django 4.1.4 on 2022-12-14 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='posted',
        ),
    ]
