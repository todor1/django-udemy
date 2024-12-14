from rest_framework import viewsets
from reporting.models import Order, Category, Supplier, Customer, Product
from reporting.serializers import (
    OrderSerializer,
    CategorySerializer,
    SupplierSerializer,
    CustomerSerializer,
    ProductSerializer,
)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by("-order_date")


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer

    def get_queryset(self):
        return Supplier.objects.all().order_by("country", "company_name")


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all().order_by("country", "last_name")


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    # ordering added as a meta class in the model
    queryset = Product.objects.all()
