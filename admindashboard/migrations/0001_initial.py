# Generated by Django 5.0.4 on 2024-06-04 07:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('file_path', models.TextField()),
                ('media_type', models.TextField(blank=True, null=True)),
                ('duration', models.IntegerField(max_length=50)),
                ('position', models.CharField(choices=[('main', 'Main'), ('detail_page', 'Detail Page')], max_length=50)),
                ('expire_date', models.DateField()),
                ('fee', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ads_posted', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ads',
            },
        ),
    ]
