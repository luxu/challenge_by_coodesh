# Generated by Django 4.0 on 2022-03-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voos', '0014_voo_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voo',
            name='key',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
