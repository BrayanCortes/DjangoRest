# Generated by Django 4.0.4 on 2022-04-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0007_alter_alimento_id_alter_plato_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='NombreAlimento',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='plato',
            name='NombrePlato',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
