# Generated by Django 5.0.6 on 2024-05-25 07:10

import django.utils.crypto
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('account_id', models.CharField(max_length=50, unique=True)),
                ('account_name', models.CharField(max_length=100)),
                ('app_secret_token', models.CharField(default=django.utils.crypto.get_random_string, max_length=50)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
