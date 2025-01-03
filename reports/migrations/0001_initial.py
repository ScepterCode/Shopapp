# Generated by Django 5.1.4 on 2024-12-31 13:30

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
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file_path', models.FileField(upload_to='documents/')),
                ('description', models.TextField(blank=True, null=True)),
                ('uploaded_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uploaded_documents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_name', models.CharField(max_length=255)),
                ('report_type', models.CharField(choices=[('SALES', 'Sales Report'), ('PRODUCT', 'Product Analysis'), ('CUSTOMER', 'Customer History'), ('PAYMENT', 'Payment Report'), ('TAX', 'Tax Report')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file_path', models.FileField(upload_to='reports/')),
                ('generated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='generated_reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
