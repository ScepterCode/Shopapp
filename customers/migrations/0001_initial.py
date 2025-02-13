# Generated by Django 5.1.4 on 2024-12-31 07:27

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
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('customer_type', models.CharField(choices=[('regular', 'Regular'), ('corporate', 'Corporate'), ('wholesale', 'Wholesale')], max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('tax_number', models.CharField(blank=True, max_length=50, null=True)),
                ('credit_limit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('primary', 'Primary'), ('billing', 'Billing'), ('shipping', 'Shipping'), ('technical', 'Technical')], max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('is_primary', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='customers.customer')),
            ],
        ),
    ]
