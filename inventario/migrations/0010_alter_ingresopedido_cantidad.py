# Generated by Django 4.0.1 on 2022-03-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_lista_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresopedido',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad a Ingresar'),
        ),
    ]
