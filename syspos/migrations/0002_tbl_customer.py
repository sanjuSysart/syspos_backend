# Generated by Django 3.2.2 on 2021-12-23 06:01

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('syspos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_customer',
            fields=[
                ('cus_id', models.AutoField(primary_key=True, serialize=False)),
                ('join_date', models.DateField(auto_now=True)),
                ('first_name', models.TextField()),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email_id', models.EmailField(max_length=300, null=True)),
                ('mobile', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('address', models.TextField(null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('cus_user', models.IntegerField()),
                ('vat_number', models.CharField(max_length=200)),
                ('customer_image', models.CharField(blank=True, max_length=1200)),
                ('remark', models.TextField(null=True)),
                ('trash', models.BooleanField(default=True)),
            ],
        ),
    ]
