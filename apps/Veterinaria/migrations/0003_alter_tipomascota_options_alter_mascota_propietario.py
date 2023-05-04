# Generated by Django 4.2.1 on 2023-05-03 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Veterinaria', '0002_tipomascota_mascota'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipomascota',
            options={'ordering': ['id'], 'verbose_name': 'tipo mascota', 'verbose_name_plural': 'tipo mascotas'},
        ),
        migrations.AlterField(
            model_name='mascota',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Veterinaria.cliente', verbose_name='Propietario'),
        ),
    ]