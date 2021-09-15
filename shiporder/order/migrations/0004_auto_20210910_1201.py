# Generated by Django 3.2.7 on 2021-09-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210909_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazon_warehouses',
            name='post_code',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overseas_warehouses',
            name='company_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overseas_warehouses',
            name='email',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overseas_warehouses',
            name='name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overseas_warehouses',
            name='post_code',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overseas_warehouses',
            name='telephone',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
