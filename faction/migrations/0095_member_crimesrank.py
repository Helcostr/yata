# Generated by Django 3.0.8 on 2020-08-15 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faction', '0094_auto_20200815_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='crimesRank',
            field=models.IntegerField(default=0),
        ),
    ]
