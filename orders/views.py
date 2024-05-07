from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from .filters import OrderFilter, OrderItemFilter
from rest_framework.response import Response


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = OrderFilter
    search_fields = ['customer__username', 'total_price', 'products']
    ordering_fields = ['customer__username', 'total_price']

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'success': True}, status=204)


# class OrderItemViewSet(viewsets.ModelViewSet):
#     queryset = OrderItem.objects.all()
#     serializer_class = OrderItemSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_class = OrderItemFilter
#     search_fields = ['product__name']
#     ordering_fields = ['product__name', 'quantity']