# Generated by Django 3.1.4 on 2020-12-14 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_cameras_headphones_tv'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cameras',
            new_name='Camera',
        ),
        migrations.RenameModel(
            old_name='Headphones',
            new_name='Headphone',
        ),
    ]
