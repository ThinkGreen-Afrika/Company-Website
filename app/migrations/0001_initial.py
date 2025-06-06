# Generated by Django 5.1.1 on 2024-10-05 13:45

import app.models
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=15)),
                ('otp', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_verified', models.BooleanField(default=False)),
                ('expires_at', models.DateTimeField(default=app.models.get_expiry_time)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('business_challenges', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('funding_stage', models.CharField(blank=True, max_length=100, null=True)),
                ('number_of_employees', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talent_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('country_of_residence', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('resume', models.FileField(upload_to='resumes/')),
                ('cover_letter', models.FileField(upload_to='cover_letters/')),
                ('preferred_language', models.CharField(max_length=50)),
                ('website_or_portfolio', models.URLField(blank=True, null=True)),
                ('social_links', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
