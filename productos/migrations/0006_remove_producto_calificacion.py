# Generated by Django 4.2 on 2023-07-22 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_producto_calificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='calificacion',
        ),
    ]
