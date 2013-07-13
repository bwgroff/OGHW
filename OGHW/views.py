# from django.http import HttpResponse
from django.shortcuts import render


def frontpage(request):
    user = {'known': True, 'first_name': 'Brad', 'last_name': False}
    store = {'name':  'Store_Name', 'motto': 'Store_Motto'}
    prod1 = {'sku': 1, 'name': 'Product_Name', 'desc': 'Product_Description'}
    prod2 = {'sku': 2, 'name': 'Product_Name', 'desc': 'Product_Description'}
    prod3 = {'sku': 3, 'name': 'Product_Name', 'desc': 'Product_Description'}
    products = [prod1, prod2, prod3]
    if (user['known'] and (type(user['first_name']) != str)):
        user['known'] = False
    c = {'user': user, 'store': store, 'product_list': products}
    return render(request, 'frontpage.html', c)
