# Generated by Django 3.2.24 on 2024-02-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240213_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
        migrations.AddField(
            model_name='blog',
            name='desciption',
            field=models.CharField(max_length=40, null=True),
        ),
    ]