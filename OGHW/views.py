# from django.http import HttpResponse
from django.shortcuts import render
from StoreDB.models import Product, Customer, Purchase, Subscriptions


def frontpage(request):
    user = {'known': True, 'first_name': 'Brad', 'last_name': False}
    store = {'name':  'Store_Name', 'motto': 'Store_Motto'}
    products = Product.objects.all()
    if (user['known'] and (type(user['first_name']) != str)):
        user['known'] = False
    c = {'user': user, 'store': store, 'product_list': products}
    return render(request, 'frontpage.html', c)
