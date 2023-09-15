# Generated by Django 4.1.11 on 2023-09-15 16:09

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreModel',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('coordx', models.FloatField()),
                ('coordy', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('storeType', models.CharField(choices=[('Accom', '숙박 시설'), ('restau', '식당'), ('etc', '기타')], max_length=20)),
                ('imageSrc', models.ImageField(null=True, upload_to='store')),
                ('target', models.CharField(choices=[('ALL', '전 장병 및 군무원'), ('ADS', '현역 용사'), ('NCO', '부사관'), ('OF', '장교'), ('MC', '군무원')], max_length=3)),
                ('promotion', models.TextField(null=True)),
                ('tel', models.TextField(null=True)),
                ('facilities', models.TextField(null=True)),
                ('homepage', models.TextField(null=True)),
                ('endDate', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
    ]
