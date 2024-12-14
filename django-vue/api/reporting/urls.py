from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reporting.views import (
    OrderViewSet,
    CategoryViewSet,
    SupplierViewSet,
    CustomerViewSet,
    ProductViewSet,
)

router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="orders")
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"suppliers", SupplierViewSet, basename="suppliers")
router.register(r"customers", CustomerViewSet, basename="customers")
router.register(r"products", ProductViewSet, basename="products")


urlpatterns = [
    path("", include(router.urls)),
]
