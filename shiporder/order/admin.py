from django.contrib import admin
from .models import order_list,warehouse,overseas_warehouses,amazon_warehouses,server_model,goods_list
# Register your models here.
admin.site.register(order_list)
admin.site.register(warehouse)
admin.site.register(overseas_warehouses)
admin.site.register(amazon_warehouses)
admin.site.register(server_model)
admin.site.register(goods_list)
