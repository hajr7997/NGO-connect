# Generated by Django 5.0.2 on 2024-02-24 15:13

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
            name='ngousers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('NGO', 'NGO'), ('Donor', 'Donor'), ('Receiver', 'Receiver')], max_length=10)),
                ('phone_number', models.CharField(max_length=13, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
