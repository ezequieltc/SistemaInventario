# Generated by Django 4.0.1 on 2022-03-30 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0017_remove_venta_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='actualizado',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='creado',
        ),
    ]
