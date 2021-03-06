# Generated by Django 3.0.3 on 2020-05-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200501_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='bio',
            field=models.TextField(max_length=200, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.TextField(max_length=200, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('ini-users', 'Usuários'), ('ini-mobile', 'Mobile'), ('ini-cog', 'Engrenagem'), ('ini-rocket', 'Foguete'), ('ini-stats-up', 'Gráficos'), ('ini-layers', 'Camadas')], max_length=12, verbose_name='Ícone'),
        ),
    ]
