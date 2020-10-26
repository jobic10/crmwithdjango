from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<int:customer_id>', views.customer, name='customer'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<int:order_id>', views.update_order, name='update_order'),

]
