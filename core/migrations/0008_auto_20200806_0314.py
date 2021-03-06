# Generated by Django 2.2.9 on 2020-08-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200806_0209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Laptop'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Ícone')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-mobile', 'Mobile'), ('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuários'), ('lni-stats-up', 'Design'), ('lni-layers', 'Camadas')], max_length=12, verbose_name='Ícone'),
        ),
    ]
