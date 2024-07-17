# Generated by Django 5.0.6 on 2024-06-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nottodo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nottodo',
            old_name='scheduled_time',
            new_name='end_time',
        ),
        migrations.AddField(
            model_name='nottodo',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]