# Generated by Django 5.0 on 2023-12-13 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_hosteluser_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='CheckInDate',
            new_name='BookingDate',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='CheckOutDate',
        ),
    ]