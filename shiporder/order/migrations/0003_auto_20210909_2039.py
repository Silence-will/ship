# Generated by Django 3.2.7 on 2021-09-09 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210909_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_list',
            name='box_num',
        ),
        migrations.RemoveField(
            model_name='order_list',
            name='fba_id',
        ),
        migrations.RemoveField(
            model_name='order_list',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='order_list',
            name='goods_num',
        ),
        migrations.RemoveField(
            model_name='order_list',
            name='goods_weight',
        ),
        migrations.RemoveField(
            model_name='order_list',
            name='reference_id',
        ),
        migrations.CreateModel(
            name='order_goods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('goods', models.CharField(max_length=200)),
                ('fba_id', models.CharField(max_length=200)),
                ('reference_id', models.CharField(max_length=200)),
                ('box_num', models.IntegerField(max_length=200)),
                ('goods_num', models.IntegerField(max_length=200)),
                ('goods_weight', models.IntegerField(max_length=200)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order_list')),
            ],
        ),
    ]