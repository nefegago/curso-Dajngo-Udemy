# Generated by Django 2.1.1 on 2018-09-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='ico',
            field=models.CharField(default='fa-street-view', max_length=200, verbose_name='Ico'),
        ),
    ]
