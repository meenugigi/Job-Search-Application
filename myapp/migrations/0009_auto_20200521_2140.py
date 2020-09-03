# Generated by Django 2.1.7 on 2020-05-21 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200521_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 21, 40, 39, 94864), editable=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employerdetails',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 21, 40, 39, 94864), editable=False),
        ),
        migrations.AlterField(
            model_name='employerdetails',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 21, 40, 39, 94864), editable=False),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 21, 21, 40, 39, 94864), editable=False),
        ),
    ]