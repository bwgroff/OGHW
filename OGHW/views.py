# from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render #, render_to_response
# from django.template import RequestContext
from StoreDB.models import Product, PurchaseRecord
from django.contrib.auth import authenticate, login


def frontpage(request):
    user = request.user
    store = {'name':  'Store_Name', 'motto': 'Store_Motto'} # get this from URL
    products = Product.objects.all()
    c = {'user': user, 'store': store, 'product_list': products}
    return render(request, 'frontpage.html', c)

def history(request):
    order_history = PurchaseRecord.objects.filter(user_id=request.user.id)
    c = {'user': request.user,'orders':order_history}
    return render(request, 'history.html', c)

def checkout(request):
    pass

def viewcart(request):
    pass

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/newuser/")#/books/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })#, context_instance=RequestContext(request))

from django.contrib import auth

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

        