# Generated by Django 4.0.4 on 2022-06-24 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba3', '0005_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='cantidad',
            field=models.IntegerField(null=True, verbose_name='Cantidad de producto'),
        ),
    ]