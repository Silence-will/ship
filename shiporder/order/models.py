from django.db import models

# Create your models here.


class goods_list(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=200)
    bg_price = models.CharField(max_length=200)
    box_height = models.CharField(max_length=200)
    box_length = models.CharField(max_length=200)
    box_width = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    cn_name = models.CharField(max_length=200)
    en_name = models.CharField(max_length=200)
    hs_code = models.CharField(max_length=200)
    hts = models.CharField(max_length=200)
    is_charged = models.IntegerField()
    is_magnetic = models.IntegerField()
    material = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    qg_price = models.CharField(max_length=200)
    used = models.CharField(max_length=200)
    rate = models.CharField(max_length=200)
    tax_rate = models.CharField(max_length=200)
    imgs = models.CharField(max_length=200)


    def __str__(self):
        return self.code

class server_model(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class amazon_warehouses(models.Model):
    id = models.IntegerField( primary_key=True)
    address = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    post_code  = models.CharField(max_length=200)
    def __str__(self):
        return self.code

class overseas_warehouses(models.Model):
    id = models.IntegerField( primary_key=True)
    address = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    post_code = models.CharField(max_length=200)
    telephone = models.CharField(max_length=200)

    def __str__(self):
        return self.label

class warehouse(models.Model):
    id = models.IntegerField( primary_key=True)
    address = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class order_list(models.Model):
    id = models.AutoField(primary_key=True)
    warehouse = models.CharField(max_length=200)
    overseas_warehouses = models.CharField(max_length=200)
    amazon_warehouses = models.CharField(max_length=200)
    server_model = models.CharField(max_length=200)
    ship_date = models.CharField(max_length=200)
    is_fba = models.IntegerField()
    my_order = models.CharField(max_length=200)
    baoguan = models.IntegerField()
    qingguan = models.IntegerField()
    status = models.CharField(max_length=200)
    update_time = models.CharField(max_length=200)

    def __str__(self):
        return self.id


class order_goods(models.Model):
    id = models.AutoField(primary_key=True)
    goods = models.CharField(max_length=200)
    order_id = models.ForeignKey("order_list", on_delete=models.CASCADE)
    fba_id = models.CharField(max_length=200)
    reference_id = models.CharField(max_length=200)
    box_num = models.IntegerField()
    goods_num = models.IntegerField()
    goods_weight = models.IntegerField()
    def __str__(self):
        return self.goods














