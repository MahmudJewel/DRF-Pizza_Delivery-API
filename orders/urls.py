from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewset

router = DefaultRouter()
router.register('list', OrderViewset, basename='list')

urlpatterns = [
    path('', include(router.urls))
]