# Generated by Django 2.0.5 on 2019-08-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0054_wall'),
    ]

    operations = [
        migrations.AddField(
            model_name='wall',
            name='defenderFactionId',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wall',
            name='defenderFactionName',
            field=models.CharField(default='DefendFaction', max_length=200),
        ),
        migrations.AlterField(
            model_name='wall',
            name='attackerFactionName',
            field=models.CharField(default='AttackFaction', max_length=200),
        ),
    ]