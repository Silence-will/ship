# Generated by Django 3.2.7 on 2021-09-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_server_model_shipping_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_list',
            name='rate',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods_list',
            name='tax_rate',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amazon_warehouses',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='goods_list',
            name='is_charged',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='goods_list',
            name='is_magnetic',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order_goods',
            name='box_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order_goods',
            name='goods_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order_goods',
            name='goods_weight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order_list',
            name='baoguan',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order_list',
            name='is_fba',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order_list',
            name='qingguan',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='overseas_warehouses',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='server_model',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
