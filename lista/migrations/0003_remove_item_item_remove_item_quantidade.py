# Generated by Django 5.0 on 2023-12-06 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0002_item_quantidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item',
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantidade',
        ),
    ]