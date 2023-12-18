# Generated by Django 4.0.5 on 2022-08-28 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prison', '0002_delete_crime'),
        ('record', '0006_remove_criminal_prisonname'),
    ]

    operations = [
        migrations.AddField(
            model_name='criminal',
            name='PrisonName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prison.prison'),
        ),
    ]
