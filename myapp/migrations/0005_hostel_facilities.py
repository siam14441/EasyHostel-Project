# Generated by Django 5.0 on 2023-12-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_room_roomimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='facilities',
            field=models.ManyToManyField(related_name='hostels', through='myapp.HostelFacility', to='myapp.facility'),
        ),
    ]
