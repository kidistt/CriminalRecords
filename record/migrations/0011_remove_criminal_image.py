# Generated by Django 4.1.1 on 2022-09-20 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0010_criminal_image_remove_criminal_crime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminal',
            name='Image',
        ),
    ]