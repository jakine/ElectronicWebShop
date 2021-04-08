from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    context = {}
    return render(request, 'store/base.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        item = order.orderitem_set.all()
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)





def store(request):

    # getting all the attributes from products database
    products = Product.objects.all()
    context = { 'products':products}
    return render(request, 'store/store.html', context)