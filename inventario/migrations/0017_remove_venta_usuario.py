# Generated by Django 4.0.1 on 2022-03-30 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0016_alter_venta_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='usuario',
        ),
    ]
