# Generated by Django 3.2.24 on 2024-02-16 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20240214_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='register_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.register'),
            preserve_default=False,
        ),
    ]
