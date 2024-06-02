from rest_framework import generics
from .models import MenuItem, Category
from .serializers import MenuItemSerializer, CategorySerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAuthenticated


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticated]
    ordering_fields = ['price', 'inventory']
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']
