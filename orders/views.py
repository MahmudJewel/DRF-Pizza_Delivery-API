from django.shortcuts import render
from orders.models import Order
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth import get_user_model
from orders.serializers import OrderSerializer, OrderStatusUpdateSerializer
from rest_framework import viewsets

User=get_user_model()

# Create your views here.

class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes=[IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        data=request.data
        new_obj = Order.objects.create(order_status='PENDING', 
                                    size=data['size'],
                                    quantity=data['quantity'],
                                    flavour=data['flavour'], 
                                    customer=request.User)
        new_obj.save()
        serializer = OrderSerializer(new_obj)
        return Response(serializer.data)
        
