from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, "account/dashboard.html", context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "account/products.html", context)


def customer(request, customer_id):
    context = {}
    return render(request, "account/customer.html", context)
