# Generated by Django 4.0 on 2021-12-12 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voos', '0010_alter_events_key_alter_events_provider_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voo',
            name='launches',
        ),
    ]
