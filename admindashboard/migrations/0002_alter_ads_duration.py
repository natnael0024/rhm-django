# Generated by Django 5.0.4 on 2024-06-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='duration',
            field=models.IntegerField(),
        ),
    ]