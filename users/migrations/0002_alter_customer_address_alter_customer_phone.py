# Generated by Django 5.0 on 2024-05-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
