# Generated by Django 3.0.1 on 2020-01-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0031_key_tid'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='useFact',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='key',
            name='useSelf',
            field=models.BooleanField(default=True),
        ),
    ]