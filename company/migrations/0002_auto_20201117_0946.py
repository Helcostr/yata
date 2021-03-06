# Generated by Django 3.1.2 on 2020-11-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='end_gain',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='end_required',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='int_gain',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='int_required',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='man_gain',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='man_required',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='position',
            name='special_ability',
            field=models.CharField(default='Default sepcial ability', max_length=32),
        ),
        migrations.AddField(
            model_name='special',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='special',
            name='rating_required',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='rating_required',
            field=models.IntegerField(default=0),
        ),
    ]
