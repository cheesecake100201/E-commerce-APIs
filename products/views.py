from rest_framework import viewsets, filters, mixins
from rest_framework.permissions import IsAuthenticated
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer
from .models import Product
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price']

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'success': True}, status=204)