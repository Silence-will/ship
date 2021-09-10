from django.shortcuts import render
from django.http import HttpResponse
from .models import warehouse, amazon_warehouses, overseas_warehouses,server_model,goods_list,order_list,order_goods
import json
import requests
from operator import itemgetter
# Create your views here.

def get_headers():
    headers_str = """Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6
Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9uYXBpLnUtc2hpcG1lbnQuY29tXC9mcm9udFwvYXV0aFwvbG9naW4iLCJpYXQiOjE2MzExNzk2MTMsImV4cCI6MTY2MjcxNTYxMywibmJmIjoxNjMxMTc5NjEzLCJqdGkiOiJCZHB2NmZBVmNXeXpCZTB1Iiwic3ViIjoxMjg2LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.NE5f-9OUtkMbYRLOUwu_pjRA4uvEv7CU8Wc-AQjCO1s
Connection: keep-alive
Host: napi.u-shipment.com
Origin: http://service.u-shipment.com
Referer: http://service.u-shipment.com/
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"""
    headers = dict()
    for item in headers_str.split("\n"):
        k,v = item.split(":", 1)
        headers[k.strip()] = v.strip()
    return headers

def update_server_model():
    res = requests.get("http://napi.u-shipment.com/front/order/prdList?warehouse_id=1&post_code=18031&start_mode[]=1&start_mode[]=2&fba_code=ABE2&end_mode[]=H_EXPRESS&end_mode[]=H_TRUCK", headers=get_headers())
    product_list_to_insert = list()
    for x in res.json()['data']['list']:
        product_list_to_insert.append(server_model(id=x['id'], name=x['name']))
    server_model.objects.bulk_create(product_list_to_insert, ignore_conflicts=True)
    return HttpResponse('ok')

def update_goods():
    res = requests.get("http://napi.u-shipment.com/front/user/product?key=&page=1", headers=get_headers())
    product_list_to_insert = list()
    for x in res.json()['data']['list']['data']:
        product_list_to_insert.append(goods_list(**x))
    goods_list.objects.bulk_create(product_list_to_insert, ignore_conflicts=True)
    return HttpResponse('ok')

def update_house():
    res = requests.get("http://napi.u-shipment.com/front/order/create", headers=get_headers())

    product_list_to_insert = list()
    for x in res.json()['data']['warehouse']:
        product_list_to_insert.append(warehouse(**x))
    warehouse.objects.bulk_create(product_list_to_insert, ignore_conflicts=True)

    product_list_to_insert = list()
    for x in res.json()['data']['overseas_warehouses']:
        product_list_to_insert.append(overseas_warehouses(**x))
    overseas_warehouses.objects.bulk_create(product_list_to_insert, ignore_conflicts=True)

    product_list_to_insert = list()
    for x in res.json()['data']['amazon_warehouses']:
        product_list_to_insert.append(amazon_warehouses(**x))
    amazon_warehouses.objects.bulk_create(product_list_to_insert, ignore_conflicts=True)



    return HttpResponse('ok')

def get_server_model():
    models = server_model.objects.all()
    server_model_lst = []
    for model in models:
        server_model_lst.append(model.name)
    return HttpResponse(json.dumps({'server_model':server_model_lst}))

def get_warehouse():
    houses = warehouse.objects.all()
    warehouse_lst = []
    for house in houses:
        warehouse_lst.append(house.name)
    return HttpResponse(json.dumps({'warehouse':warehouse_lst}))

def get_overseas_warehouses():
    houses = overseas_warehouses.objects.all()
    house_lst = []
    for house in houses:
        house_lst.append(house.label)
    return HttpResponse(json.dumps({'overseas_warehouses':house_lst}))

def get_amazon_warehouses():
    houses = amazon_warehouses.objects.all()
    house_lst = []
    for house in houses:
        house_lst.append(house.code)
    return HttpResponse(json.dumps({'amazon_warehouses':house_lst}))

def get_goods():
    goodss = goods_list.objects.all()
    goods_lst = []
    for goods in goodss:
        goods_lst.append(goods.code)
    return HttpResponse(json.dumps({'goods':goods_lst}))


def index(request):
    return render(request, "order/index.html")


def get_data(request):
    if request.GET['data_header'] == "warehouse":
        return get_warehouse()
    elif request.GET['data_header'] == "overseas_warehouses":
        return get_overseas_warehouses()
    elif request.GET['data_header'] == "amazon_warehouses":
        return get_amazon_warehouses()
    elif request.GET['data_header'] == "server_model":
        return get_server_model()
    elif request.GET['data_header'] == "goods":
        return get_goods()



def update_data(request):
    if request.GET['data_header'] == "goods":
        return update_goods()
    elif request.GET['data_header'] == "warehouse":
        return update_house()
    elif request.GET['data_header'] == "server":
        return update_server_model()
    elif request.GET['data_header'] == "goods":
        return update_goods()

def order_ship(request):
    data_dic = {
        "warehouse":request.POST['warehouse'],
        "overseas_warehouses":request.POST['overseas_warehouses'],
        "amazon_warehouses":request.POST['amazon_warehouses'],
        "server_model": request.POST['server_model'],
        "ship_date": request.POST['ship_date'],
        "baoguan": request.POST['baoguan'],
        "qingguan": request.POST['qingguan'],

    }
    aa = order_list.objects.create(**data_dic)
    aa.save()
    goods_dic = {
        "goods_selects": request.POST.getlist("goods_selects"),
        "FBAID_selects": request.POST.getlist("FBAID_selects"),
        "referenceID_selects": request.POST.getlist("referenceID_selects"),
        "boxNum_selects": request.POST.getlist("boxNum_selects"),
        "goodsNum_selects": request.POST.getlist("goodsNum_selects"),
        "goodsWeight_selects": request.POST.getlist("goodsWeight_selects"),
    }



    print(data_dic)


