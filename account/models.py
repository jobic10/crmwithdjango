from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
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
    tag = models.ManyToManyField(Tag)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    ]
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=18, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)
