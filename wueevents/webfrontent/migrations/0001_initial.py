# Generated by Django 3.0.5 on 2020-04-06 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('enabled', models.BooleanField(default=True)),
                ('schedule', models.CharField(choices=[('D', 'Daily'), ('H', 'Hourly'), ('W', 'Weekly')], default='W', max_length=1)),
                ('start_date', models.DateField()),
                ('latitude', models.CharField(max_length=20, null=True)),
                ('longitude', models.CharField(max_length=20, null=True)),
                ('street', models.CharField(max_length=200, null=True)),
                ('zip_code', models.CharField(max_length=5, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]