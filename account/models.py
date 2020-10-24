from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=70, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
