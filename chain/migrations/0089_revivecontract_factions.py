# Generated by Django 3.0.1 on 2020-01-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0088_revivecontract_first'),
    ]

    operations = [
        migrations.AddField(
            model_name='revivecontract',
            name='factions',
            field=models.TextField(default='{}'),
        ),
    ]