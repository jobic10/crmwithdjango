from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(
        null=True, blank=True, default="profile.jpg")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = [
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    ]
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField()
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    ]
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=18, choices=STATUS, default='Pending')
    date_created = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer}  ordered {self.product} with status : {self.status}"
