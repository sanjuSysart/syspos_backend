# Generated by Django 3.2.2 on 2021-12-23 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syspos', '0002_tbl_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='address',
            new_name='cus_address',
        ),
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='email_id',
            new_name='cus_email',
        ),
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='first_name',
            new_name='cus_first_name',
        ),
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='customer_image',
            new_name='cus_image',
        ),
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='join_date',
            new_name='cus_join_date',
        ),
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='last_name',
            new_name='cus_last_name',
        ),
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='mobile',
            new_name='cus_mobile',
        ),
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='password',
            new_name='cus_password',
        ),
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='remark',
            new_name='cus_remark',
        ),
        migrations.RenameField(
            model_name='tbl_customer',
            old_name='vat_number',
            new_name='cus_vat',
        ),
    ]
