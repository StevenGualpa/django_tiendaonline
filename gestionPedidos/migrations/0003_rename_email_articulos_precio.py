# Generated by Django 4.1.1 on 2022-09-27 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_alter_clientes_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulos',
            old_name='email',
            new_name='precio',
        ),
    ]