import django_filters
from .models import Order, OrderItem

class OrderFilter(django_filters.FilterSet):
    customer__user__username = django_filters.CharFilter(lookup_expr='icontains')
    total_price = django_filters.RangeFilter()

    class Meta:
        model = Order
        fields = ['customer', 'total_price']

class OrderItemFilter(django_filters.FilterSet):
    product__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']