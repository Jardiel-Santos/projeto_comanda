# Generated by Django 5.0.4 on 2024-05-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0009_remove_bebida_valor_prato_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prato',
            name='foto',
            field=models.ImageField(upload_to='fotos_pratos'),
        ),
    ]
