# Generated by Django 2.2.15 on 2021-03-18 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200806_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-layers', 'Camadas'), ('lni-leaf', 'Folha'), ('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Laptop')], max_length=16, verbose_name='Ícone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-users', 'Usuários'), ('lni-cog', 'Engrenagem'), ('lni-layers', 'Camadas'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-stats-up', 'Design')], max_length=12, verbose_name='Ícone'),
        ),
    ]