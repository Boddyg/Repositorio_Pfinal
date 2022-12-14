# Generated by Django 4.1.4 on 2022-12-14 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_post', '0002_remove_article_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]