import django_filters
from .models import Customer

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'address', 'phone']
