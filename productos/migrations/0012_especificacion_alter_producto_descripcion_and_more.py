# Generated by Django 4.2 on 2023-07-26 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_especificacionproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='EspecificacionProducto',
        ),
        migrations.AddField(
            model_name='especificacion',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='especificaciones', to='productos.producto'),
        ),
    ]
