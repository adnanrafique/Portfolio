# Generated by Django 5.0.2 on 2024-02-28 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_person_image1_person_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='website',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]