# Generated by Django 2.2 on 2019-04-15 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_busdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BusDetails',
            new_name='BusDetail',
        ),
        migrations.RenameModel(
            old_name='Songs',
            new_name='Song',
        ),
    ]
