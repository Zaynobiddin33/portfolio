# Generated by Django 5.0.1 on 2024-01-21 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='sent_time',
        ),
    ]
