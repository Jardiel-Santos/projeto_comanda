# Generated by Django 5.0.4 on 2024-05-15 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0006_rename_fotografia_bebida_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='foto',
            field=models.ImageField(upload_to='fotos_bebidas'),
        ),
        migrations.AlterField(
            model_name='prato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos_pratos'),
        ),
    ]
