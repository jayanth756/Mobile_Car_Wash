# Generated by Django 4.1.3 on 2022-11-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_rename_room_number_appointment_vechilenum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='vechilenum',
            field=models.CharField(max_length=51),
        ),
    ]