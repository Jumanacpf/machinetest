# Generated by Django 3.2.24 on 2024-02-14 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20240213_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='desciption',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='register_id',
        ),
    ]
