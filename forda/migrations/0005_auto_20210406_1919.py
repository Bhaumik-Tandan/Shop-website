# Generated by Django 3.1.7 on 2021-04-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forda', '0004_auto_20210406_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, height_field=600, upload_to='', width_field=510),
        ),
    ]
