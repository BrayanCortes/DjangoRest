# Generated by Django 4.0.4 on 2022-04-28 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_alimentos_platos_delete_filosofos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='alimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alimento', to='quickstart.alimentos'),
        ),
    ]