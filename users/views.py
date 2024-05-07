from rest_framework import viewsets, filters, generics, permissions
from .filters import CustomerFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Customer
from .serializers import CustomerSerializer, UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CustomerFilter
    search_fields = ['username', 'address', 'phone']
    ordering_fields = ['username', 'address', 'phone']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAccountOwner()]
        elif self.action == 'create':
            if self.request.user.is_authenticated:
                return [permissions.IsAdminUser()]
            else:
                return [permissions.AllowAny()]
        return [IsAuthenticated()]

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({'success': True}, status=204)

class IsAccountOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an account to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object
        return obj == request.user

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

