# Generated by Django 4.0.4 on 2022-04-28 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_alter_platos_alimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlimentosRes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreAlimento', models.CharField(max_length=100)),
                ('Categoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PlatosRes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombrePlato', models.CharField(max_length=100)),
                ('Tiempo_Pre', models.IntegerField()),
                ('CategoriaP', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='platos',
            name='alimento',
        ),
        migrations.DeleteModel(
            name='Alimentos',
        ),
        migrations.DeleteModel(
            name='Platos',
        ),
        migrations.AddField(
            model_name='alimentosres',
            name='plato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alimentos', to='quickstart.platosres'),
        ),
    ]
