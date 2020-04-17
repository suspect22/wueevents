# Generated by Django 3.0.5 on 2020-04-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webfrontent', '0002_auto_20200416_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementmapping',
            name='name',
            field=models.CharField(choices=[('summary', 'Summary'), ('tend', 'End Time'), ('dtend', 'End Date'), ('tstart', 'Start Time'), ('dtstart', 'Start Date'), ('details', 'Details'), ('link', 'Source Link')], default='summary', max_length=20),
        ),
    ]
