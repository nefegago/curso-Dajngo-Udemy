# Generated by Django 2.1.1 on 2018-09-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='content',
            field=models.TextField(default=1, verbose_name='Contenido'),
            preserve_default=False,
        ),
    ]