# Generated by Django 2.1.1 on 2018-09-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_publication_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
    ]
