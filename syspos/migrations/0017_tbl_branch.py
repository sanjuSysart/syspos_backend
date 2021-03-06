# Generated by Django 3.2.2 on 2022-01-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syspos', '0016_auto_20220103_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_branch',
            fields=[
                ('br_id', models.AutoField(primary_key=True, serialize=False)),
                ('br_name', models.CharField(max_length=300)),
                ('br_pin', models.CharField(max_length=100, null=True)),
                ('br_country', models.CharField(max_length=200)),
                ('br_vat', models.CharField(max_length=300, null=True)),
                ('br_gst', models.CharField(max_length=200, null=True)),
                ('br_email', models.EmailField(max_length=300)),
                ('br_phone', models.BigIntegerField()),
                ('br_address', models.CharField(max_length=300, null=True)),
                ('br_city', models.CharField(max_length=200, null=True)),
                ('br_state', models.CharField(max_length=200)),
                ('br_description', models.TextField(max_length=600)),
                ('br_date', models.DateTimeField(auto_now_add=True)),
                ('trash', models.BooleanField(default=False)),
            ],
        ),
    ]
