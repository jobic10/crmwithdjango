from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *
from django.contrib import messages
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
    customer = get_object_or_404(Customer, id=customer_id)
    orders = customer.order_set.all()
    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': orders.count()
    }
    return render(request, "account/customer.html", context)


def create_order(request):
    form = OrderForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Order created successfully!")
            return redirect('/')
    return render(request, 'account/order_form.html', context)
