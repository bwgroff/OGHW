import datetime
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from StoreDB.models import Product, PurchaseRecord
# from django.contrib.auth import authenticate, login


def frontpage(request):                 # Basic landing page, changes depending on login
    user = request.user
    store = {'name':  'Store_Name', 'motto': 'Store_Motto'}
    products = Product.objects.all()
    c = {'user': user, 'store': store, 'product_list': products}
    return render(request, 'frontpage.html', c)


def history(request):                   # shows all entries of PurchaseRecord for given userid
    try:
        int(request.user.id)
        order_history = PurchaseRecord.objects.filter(user_id=request.user.id).order_by('-order_date')
        c = {'user': request.user, 'orders': order_history}
        return render(request, 'history.html', c)
    except:
        return render(request, 'record_error.html')


def product_page(request, prod_id):     # page where order for a given product is placed
    NoSuchProduct = False
    prod = 0
    try:
        prod_id = int(prod_id)
        prod = Product.objects.get(id=prod_id)
    except:
        NoSuchProduct = True
    c = {'product': prod, 'NoProd': NoSuchProduct}
    return render(request, 'product_page.html', c)


def purchase(request):                  # accepts form data from product page to update records
    req_path = request.get_full_path()
    ParseError = False
    try:
        assert request.user.id
        prod_id, quantity = req_path.split('/')[-2:]
        quantity = int(quantity.split('=')[1])
        assert quantity > 0
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
            bill=total_cost, paid=False, fulfilled=False)
        purchase.save()
    return render(request, 'purchase.html', c)


def register(request):                  # new user creation
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })  # , context_instance=RequestContext(request))
