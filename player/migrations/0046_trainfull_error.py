# Generated by Django 3.0.4 on 2020-05-04 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0045_trainfull_single_train'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainfull',
            name='error',
            field=models.FloatField(default=0.0),
        ),
    ]
