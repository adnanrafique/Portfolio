# Generated by Django 5.0.2 on 2024-02-23 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='admin_name',
        ),
    ]