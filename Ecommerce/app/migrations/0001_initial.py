# Generated by Django 5.1.2 on 2024-10-28 06:41

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
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('image_path', models.CharField(max_length=255)),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Phones',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_address', models.CharField(max_length=200)),
                ('customer_city', models.CharField(max_length=50)),
                ('customer_zip_code', models.CharField(max_length=5)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer_phone', models.CharField(max_length=11)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.phone')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30)),
                ('display', models.CharField(max_length=35)),
                ('resolution', models.CharField(max_length=20)),
                ('processor', models.CharField(max_length=35)),
                ('ram', models.CharField(max_length=15)),
                ('storage', models.CharField(max_length=50)),
                ('rear_camera', models.CharField(max_length=50)),
                ('front_camera', models.CharField(max_length=15)),
                ('battery', models.CharField(max_length=10)),
                ('operating_system', models.CharField(max_length=30)),
                ('dimensions', models.CharField(max_length=35)),
                ('weight', models.CharField(max_length=20)),
                ('connectivity', models.CharField(max_length=30)),
                ('colors', models.CharField(max_length=100)),
                ('phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.phone')),
            ],
        ),
    ]
