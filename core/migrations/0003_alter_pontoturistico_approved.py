# Generated by Django 3.2.7 on 2021-09-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_is_aprove_pontoturistico_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]