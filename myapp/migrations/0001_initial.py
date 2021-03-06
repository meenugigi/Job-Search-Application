# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-20 10:26
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_webuser', models.BooleanField(default=False)),
                ('is_employer', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('description', models.TextField()),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(default=datetime.datetime(2020, 5, 20, 15, 56, 15, 567850), editable=False)),
                ('fresher', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AvailablePosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployerDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('about_us', models.TextField()),
                ('strength', models.IntegerField()),
                ('vacancies', models.IntegerField()),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2020, 5, 20, 15, 56, 15, 565851), editable=False)),
                ('updated', models.DateTimeField(default=datetime.datetime(2020, 5, 20, 15, 56, 15, 565851), editable=False)),
                ('availableposts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.AvailablePosts')),
                ('companytype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.CompanyType')),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayname', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('review', models.TextField(null=True)),
                ('published_at', models.DateTimeField(default=datetime.datetime(2020, 5, 20, 15, 56, 15, 567850), editable=False)),
                ('company_name', models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.EmployerDetails')),
            ],
        ),
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employerdetails',
            name='own',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employerdetails',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='availableposts',
            name='companytype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.CompanyType'),
        ),
        migrations.AddField(
            model_name='application',
            name='availableposts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.AvailablePosts'),
        ),
        migrations.AddField(
            model_name='application',
            name='company_name',
            field=models.ForeignKey(max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.EmployerDetails'),
        ),
        migrations.AddField(
            model_name='application',
            name='companytype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.CompanyType'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
