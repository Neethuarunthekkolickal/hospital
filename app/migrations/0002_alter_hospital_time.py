# Generated by Django 4.1.5 on 2024-03-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='time',
            field=models.TimeField(),
        ),
    ]
