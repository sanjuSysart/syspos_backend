# Generated by Django 3.2.2 on 2022-01-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syspos', '0015_tbl_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_supplier',
            name='sup_address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_supplier',
            name='sup_city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_supplier',
            name='sup_country',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_supplier',
            name='sup_name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_supplier',
            name='sup_pin',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tbl_supplier',
            name='sup_state',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
