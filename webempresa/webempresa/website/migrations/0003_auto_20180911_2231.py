# Generated by Django 2.0 on 2018-09-11 22:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20180911_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Contenido'),
        ),
    ]