# Generated by Django 2.1.1 on 2018-09-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_social_ico'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='social',
            name='ico',
            field=models.CharField(default='fa-social-home', max_length=200, verbose_name='Ico'),
        ),
    ]