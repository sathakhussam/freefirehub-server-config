# Generated by Django 3.0.8 on 2020-07-18 11:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import listings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freefire_id', models.CharField(max_length=100, unique=True)),
                ('level', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=264, unique=True)),
                ('description', models.TextField()),
                ('estimated_price', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('is_sold', models.BooleanField(default=False)),
                ('signed_up_with', models.CharField(choices=[('Facebook', 'Facebook'), ('Gmail', 'Gmail'), ('VK', 'VK')], max_length=264)),
                ('account_email', models.CharField(max_length=264, unique=True)),
                ('account_password', models.CharField(max_length=264)),
                ('photo_main', models.ImageField(upload_to=listings.models.get_upload_path)),
                ('video_main', models.FileField(upload_to=listings.models.get_upload_path)),
                ('posted_date', models.DateTimeField(default=datetime.datetime.now)),
                ('seller_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TempStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=55, unique=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=55, unique=True)),
                ('purchased_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ListingAcc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.Listing', unique=True)),
                ('customer_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentsStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.BigIntegerField()),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('price', models.IntegerField()),
                ('ListingAcc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.Listing', unique=True)),
                ('customer_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]