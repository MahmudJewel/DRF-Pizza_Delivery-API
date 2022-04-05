from django.shortcuts import render
from orders.models import Order
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.contrib.auth import get_user_model
from orders.serializers import OrderSerializer, OrderStatusUpdateSerializer
from rest_framework import viewsets
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

User=get_user_model()

# Create your views here.

# get, put and post order
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
								 	customer=request.user)
		new_obj.save()
		serializer = OrderSerializer(new_obj)
		return Response(serializer.data)
	
# update order status
class UpdateOrderStatusView(APIView):
	permission_classes=[IsAuthenticated]
	def get_object(self, order_id):
		try:
			return Order.objects.get(id=order_id)
		except Order.DoesNotExist():
			return HttpResponse(status=404)

	def get(self, request, order_id): # see indivisual student
		st = self.get_object(order_id)
		serializer = OrderStatusUpdateSerializer(st)
		return Response(serializer.data)

	def put(self, request, order_id): # update
		st = self.get_object(order_id)
		serializer = OrderStatusUpdateSerializer(st, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=400)
	