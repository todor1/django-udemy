from reporting.views import ReportingViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reporting.views import OrderViewSet

router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = [
    path("reporting/", ReportingViewSet.as_view(), name="reporting"),
    path("", include(router.urls)),
]
