# Generated by Django 4.2.2 on 2023-08-05 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_endpoints', '0005_results_query_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zoning',
            fields=[
                ('location_id', models.OneToOneField(db_column='location_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='api_endpoints.taxizones')),
                ('commercial', models.FloatField()),
                ('manufacturing', models.FloatField()),
                ('park', models.FloatField()),
                ('residential', models.FloatField()),
                ('special', models.FloatField()),
                ('zone_type', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'cityframe"."zoning',
                'managed': False,
            },
        ),
    ]