# Generated by Django 3.0.1 on 2020-02-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0012_targetinfo_last_attack_attacker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetinfo',
            name='last_attack_attacker',
            field=models.BooleanField(default=True),
        ),
    ]