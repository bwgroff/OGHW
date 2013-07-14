# from django.http import HttpResponse
import datetime
# from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render  # , render_to_response
# from django.template import RequestContext
from StoreDB.models import Product, PurchaseRecord
# from django.contrib.auth import authenticate, login


def frontpage(request):
    user = request.user
    store = {'name':  'Store_Name', 'motto': 'Store_Motto'}
    products = Product.objects.all()
    c = {'user': user, 'store': store, 'product_list': products}
    return render(request, 'frontpage.html', c)


def history(request):
    order_history = PurchaseRecord.objects.filter(user_id=request.user.id).order_by('-order_date')
    c = {'user': request.user, 'orders': order_history}
    return render(request, 'history.html', c)


def product_page(request, prod_id):
    NoSuchProduct = False
    prod = 0
    try:
        prod_id = int(prod_id)
        prod = Product.objects.get(id=prod_id)
    except:
        NoSuchProduct = True
    c = {'product': prod, 'NoProd': NoSuchProduct}
    return render(request, 'product_page.html', c)


def purchase(request):  # , prod_id, quantity):
    req_path = request.get_full_path()
    ParseError = False
    try:
        prod_id, quantity = req_path.split('/')[-2:]
        quantity = int(quantity.split('=')[1])
        prod_id = int(prod_id)
        prod = Product.objects.get(id=prod_id)
        price = prod.unit_price
        total_cost = quantity * price
    except:
        ParseError = True
        quantity, prod, total_cost = 0, 0, 0
    c = {'product': prod, 'quantity': quantity, 'ParseError': ParseError, 'price': total_cost}
    if not ParseError:
        purchase = PurchaseRecord(user_id=request.user.id,
            product_id=prod, quantity=quantity,
            order_date=datetime.datetime.now(),
            bill=total_cost,paid=False,fulfilled=False)
        purchase.save()
    return render(request, 'purchase.html', c)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")  
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })  # , context_instance=RequestContext(request))
