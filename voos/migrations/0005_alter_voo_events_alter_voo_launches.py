# Generated by Django 4.0 on 2021-12-11 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voos', '0004_alter_voo_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voo',
            name='events',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voos.events'),
        ),
        migrations.AlterField(
            model_name='voo',
            name='launches',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voos.launch'),
        ),
    ]
