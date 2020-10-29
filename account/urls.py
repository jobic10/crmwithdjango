from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('products/', views.products, name='products'),
    path('customer/<int:customer_id>', views.customer, name='customer'),
    path('create_general_order/', views.create_general_order,
         name='create_general_order'),
    path('create_order/<int:customer_id>',
         views.create_order, name='create_order'),
    path('update_order/<int:order_id>', views.update_order, name='update_order'),
    path('delete_order/<int:order_id>', views.delete_order, name='delete_order'),

]
