# Generated by Django 4.1.3 on 2022-11-17 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('oportunidade_de_venda', models.BooleanField(default=True, verbose_name='Oportunida de Venda')),
            ],
            options={
                'verbose_name': 'Proprietário',
                'verbose_name_plural': 'Proprietários',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('cor', models.CharField(choices=[('amarela', 'Amarela'), ('azul', 'Azul'), ('cinza', 'Cinza')], max_length=7, verbose_name='Cor')),
                ('tipo', models.CharField(choices=[('hatch', 'Hatch'), ('sedan', 'Sedan'), ('conversivel', 'Conversível')], max_length=11, verbose_name='Tipo')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.proprietario')),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
            },
        ),
    ]
