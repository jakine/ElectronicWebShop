from django.shortcuts import render
from .models import *

from django.http import JsonResponse
import json


# Create your views here.


def index(request):
    context = {}
    return render(request, 'store/base.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(costumer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' :False}
        cartItems = order['get_card_items']
        
    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(request, 'store/cart.html', context)



def checkout(request): 
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(costumer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' :False}
        cartItems = order['get_card_items']
        
    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)





def store(request):

    # getting all the attributes from products database
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(costumer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping' :False}
        cartItems = order['get_card_items']



    products = Product.objects.all()
    context = { 'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)



def updatedItem(request):
    data = json.loads(request.body)
    productId = data['productId'] # through cookies we get in backed end the presed id f the product
    action = data['action']
    print(productId)
    print(action)


    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(costumer=customer, complete=False)     # create the order if its not created, otherwise add the quantity
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added', safe=False)