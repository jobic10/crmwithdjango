from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, "account/dashboard.html", context)


def products(request):
    context = {}
    return render(request, "account/products.html", context)


def customer(request):
    context = {}
    return render(request, "account/customer.html", context)
