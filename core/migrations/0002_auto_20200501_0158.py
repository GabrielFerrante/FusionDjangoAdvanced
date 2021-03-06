# Generated by Django 3.0.3 on 2020-05-01 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='criados',
            new_name='criado',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='criados',
            new_name='criado',
        ),
        migrations.RenameField(
            model_name='servico',
            old_name='criados',
            new_name='criado',
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('ini-users', 'Usuários'), ('ini-cog', 'Engrenagem'), ('ini-rocket', 'Foguete'), ('ini-mobile', 'Mobile'), ('ini-stats-up', 'Gráficos'), ('ini-layers', 'Camadas')], max_length=12, verbose_name='Ícone'),
        ),
    ]
