# Generated by Django 3.0.14 on 2022-07-31 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='update',
            new_name='updated',
        ),
    ]
