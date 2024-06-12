# Generated by Django 5.0.2 on 2024-06-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_alter_person_document_alter_person_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.FileField(upload_to='portfolio/media/portfolio/documents/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='portfolio/media/portfolio/images/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image1',
            field=models.ImageField(upload_to='portfolio/media/portfolio/images/'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image2',
            field=models.ImageField(upload_to='portfolio/media/portfolio/images/'),
        ),
    ]