# Generated by Django 4.2.1 on 2023-06-29 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seguro', '0002_producto_rename_seguro_seguro_nombre_and_more'),
        ('modalidad', '0003_remove_modalidad_empresa_alter_modalidad_seguro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modalidad',
            name='seguro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seguro.tiposeguro'),
        ),
    ]
