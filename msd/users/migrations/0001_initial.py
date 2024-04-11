# Generated by Django 4.2.6 on 2023-11-08 06:39

import django.utils.timezone
from django.db import migrations, models

import msd.users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(blank=True, null=True, verbose_name='last login'),
                ),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                (
                    'email',
                    models.EmailField(
                        blank=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name='email address',
                    ),
                ),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_vendor', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                (
                    'gender',
                    models.CharField(
                        blank=True,
                        choices=[
                            ('Male', 'Male'),
                            ('Female', 'Female'),
                            ('Other', 'Other'),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    'profile_picture',
                    models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
                ),
                (
                    'mobile_number',
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        unique=True,
                        validators=[msd.users.models.validate_mobile_number],
                    ),
                ),
                ('email_verified', models.BooleanField(default=False)),
                ('phone_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(default='Unknown', max_length=255)),
                ('is_routable', models.BooleanField(default=False)),
                (
                    'verification_code',
                    models.CharField(blank=True, max_length=6, null=True),
                ),
                (
                    'verification_code_expiry',
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    'latitude',
                    models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
                ),
                (
                    'longitude',
                    models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
                ),
                (
                    'groups',
                    models.ManyToManyField(
                        blank=True,
                        help_text='The groups this user belongs to. '
                        'A user will get all permissions granted to each of their groups.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.group',
                        verbose_name='groups',
                    ),
                ),
                (
                    'user_permissions',
                    models.ManyToManyField(
                        blank=True,
                        help_text='Specific permissions for this user.',
                        related_name='user_set',
                        related_query_name='user',
                        to='auth.permission',
                        verbose_name='user permissions',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]