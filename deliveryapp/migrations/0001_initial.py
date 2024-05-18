# Generated by Django 5.0.1 on 2024-05-18 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliverer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, unique=True)),
                ('from_location', models.CharField(max_length=200)),
                ('to_location', models.CharField(max_length=200)),
                ('pick_up_location', models.CharField(max_length=200)),
                ('pick_up_pic', models.ImageField(blank=True, null=True, upload_to='pick_up_pics/')),
                ('pick_up_phone_number', models.CharField(max_length=15)),
                ('pick_up_time', models.CharField(max_length=50)),
                ('package_type', models.CharField(max_length=50)),
                ('pick_up_comment', models.TextField(blank=True, null=True)),
                ('delivery_location', models.CharField(max_length=200)),
                ('delivery_pic', models.ImageField(blank=True, null=True, upload_to='delivery_pics/')),
                ('delivery_phone_number', models.CharField(max_length=15)),
                ('delivery_time', models.CharField(max_length=50)),
                ('delivery_comment', models.TextField(blank=True, null=True)),
                ('deliverer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='deliveryapp.deliverer')),
            ],
        ),
    ]