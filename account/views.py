from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as LOGIN, logout as LOGOUT
from .forms import *
from .models import *
from .filters import *
from .decorators import *


@login_required
@admin_only
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


@login_required
def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "account/products.html", context)


@login_required
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


@login_required
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


@login_required
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


@login_required
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


@login_required
def delete_order(request, order_id):
    item = get_object_or_404(Order, id=order_id)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Order deleted!')
        return redirect('/')
    return render(request, 'account/delete.html', context)


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid credentials")
        else:
            LOGIN(request, user)
            messages.success(request, "Welcome back!")

            return redirect(reverse('home'))
    return render(request, 'account/login.html')


@unauthenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    form = CreateUserForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()

            messages.success(request, "You are now registered!")
            return redirect(reverse('login'))
        else:
            messages.error(request, "Please fix form errors!")
    return render(request, 'account/register.html', context)


def logout(request):
    if request.user.is_authenticated:
        LOGOUT(request)
        messages.success(request, "Thanks for the time!")
    else:
        messages.error(request, 'You need to be signed in to sign out')
    return redirect(reverse('login'))


@login_required
@allowed_users(allowed_roles=['customer'])
def userpage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, "account/user.html", context)


@login_required
@allowed_users(allowed_roles=['customer'])
def account_settings(request):
    form = CustomerForm(request.POST or None,
                        request.FILES or None, instance=request.user.customer)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated!")
            return redirect(reverse('account'))
        else:
            messages.error(request, 'Form has error(s), please fix!')
    return render(request, 'account/account_settings.html', context)
