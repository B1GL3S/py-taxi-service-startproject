# Generated by Django 5.0.1 on 2024-03-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.IntegerField(unique=True),
        ),
    ]
