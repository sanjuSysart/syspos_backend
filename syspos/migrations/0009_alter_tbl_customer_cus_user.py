# Generated by Django 3.2.2 on 2021-12-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syspos', '0008_alter_tbl_customer_cus_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_customer',
            name='cus_user',
            field=models.IntegerField(null=True),
        ),
    ]