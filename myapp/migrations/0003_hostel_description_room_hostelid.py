# Generated by Django 5.0 on 2023-12-12 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_hostel_hostelimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='Description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='HostelID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.hostel'),
        ),
    ]
