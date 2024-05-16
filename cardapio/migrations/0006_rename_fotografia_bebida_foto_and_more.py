# Generated by Django 5.0.4 on 2024-05-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0005_alter_bebida_fotografia_alter_prato_fotografia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bebida',
            old_name='fotografia',
            new_name='foto',
        ),
        migrations.RemoveField(
            model_name='prato',
            name='fotografia',
        ),
        migrations.AddField(
            model_name='prato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media/fotos_pratos'),
        ),
    ]