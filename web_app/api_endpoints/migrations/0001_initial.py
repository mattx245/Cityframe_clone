# Generated by Django 4.2.2 on 2023-07-19 12:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherFc',
            fields=[
                ('dt', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dt_iso', models.DateTimeField()),
                ('temp', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('visibility', models.IntegerField()),
                ('wind_speed', models.FloatField()),
                ('wind_deg', models.IntegerField()),
                ('wind_gust', models.FloatField()),
                ('rain_1h', models.FloatField(blank=True, null=True)),
                ('snow_1h', models.FloatField(blank=True, null=True)),
                ('clouds_all', models.IntegerField()),
                ('weather_id', models.IntegerField()),
                ('weather_main', models.CharField(max_length=255)),
                ('weather_description', models.CharField(max_length=255)),
                ('weather_icon', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cityframe"."weather_fc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeatherCurrent',
            fields=[
                ('dt', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dt_iso', models.DateTimeField(default=django.utils.timezone.now)),
                ('temp', models.FloatField(default=0)),
                ('feels_like', models.FloatField(default=0)),
                ('temp_min', models.FloatField(default=0)),
                ('temp_max', models.FloatField(default=0)),
                ('pressure', models.IntegerField(default=0)),
                ('humidity', models.IntegerField(default=0)),
                ('visibility', models.IntegerField(default=0)),
                ('wind_speed', models.FloatField(default=0)),
                ('wind_deg', models.IntegerField(default=0)),
                ('clouds_all', models.IntegerField(default=0)),
                ('weather_id', models.IntegerField(default=0)),
                ('weather_main', models.CharField(max_length=200)),
                ('weather_description', models.CharField(max_length=200)),
                ('weather_icon', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'cityframe_django"."weather_current',
                'managed': False,
            },
        ),
    ]
