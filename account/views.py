from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.forms import inlineformset_factory
from .forms import *
from .models import *
from .filters import *

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
    filter = OrderFilter(request.GET, queryset=orders)
    orders = filter.qs
    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': orders.count(),
        'filter': filter
    }
    return render(request, "account/customer.html", context)


def create_order(request, customer_id):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'))
    customer = get_object_or_404(Customer, id=customer_id)
    # form = OrderForm(request.POST or None, initial={'customer': customer})
    formset = OrderFormSet(request.POST or None,
                           instance=customer, queryset=Order.objects.none())
    context = {'form': formset}
    if request.method == 'POST':
        if formset.is_valid():
            formset.save()
            messages.success(request, "Order created successfully!")
            return redirect(reverse('customer', args=[customer.id]))
        else:
            messages.error(request, "Invalid Form Submitted")
    return render(request, 'account/order_form.html', context)


def create_general_order(request):
    form = OrderForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Order created successfully!")
            return redirect(reverse('create_general_order'))
        else:
            messages.error(request, "Invalid Form Submitted")
    return render(request, 'account/order_form.html', context)


def update_order(request, order_id):
    instance = get_object_or_404(Order, id=order_id)
    form = OrderForm(request.POST or None, instance=instance)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Order updated successfully!")
            return redirect(reverse('update_order', args=[order_id]))
        else:
            messages.error(request, "Invalid Form Submitted")
    return render(request, 'account/order_form.html', context)


def delete_order(request, order_id):
    item = get_object_or_404(Order, id=order_id)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Order deleted!')
        return redirect('/')
    return render(request, 'account/delete.html', context)
