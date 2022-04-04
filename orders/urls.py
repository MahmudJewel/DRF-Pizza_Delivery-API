from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewset, UpdateOrderStatusView

router = DefaultRouter()
router.register('list', OrderViewset, basename='list')

urlpatterns = [
    path('', include(router.urls)),
    path('update-status/<int:order_id>/', UpdateOrderStatusView.as_view(), name='update_order_status')
]