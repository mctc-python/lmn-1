# Generated by Django 3.1.2 on 2020-11-18 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='show_time',
            field=models.TimeField(default='00:00:00'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='show',
            name='show_date',
            field=models.DateField(),
        ),
    ]
