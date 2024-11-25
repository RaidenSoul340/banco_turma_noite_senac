# Generated by Django 5.1.3 on 2024-11-14 00:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=256)),
                ('telefone', models.CharField(max_length=11)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id_conta', models.AutoField(primary_key=True, serialize=False)),
                ('nr_conta', models.CharField(max_length=5)),
                ('nr_agencia', models.CharField(max_length=3)),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True)),
                ('tipo_conta', models.CharField(choices=[('Corrente', 'Corrente'), ('Poupanca', 'Poupanca')], max_length=10)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id_movimento', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_movimento', models.CharField(choices=[('Credito', 'Credito'), ('Debito', 'Debito')], max_length=10)),
                ('valor', models.FloatField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('id_conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.conta')),
            ],
        ),
    ]
