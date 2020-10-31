from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('user/', views.userpage, name='userpage'),
    path('account/', views.account_settings, name='account'),

    # Start of password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset/password_reset.html'),
         name='reset_password'),
    path('password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset/password_reset_form.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset/password_reset_done.html'),
         name='password_reset_complete'),

]
