from .models import *
import django_filters


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'
