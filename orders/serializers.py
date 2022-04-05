from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    order_status=serializers.HiddenField(default="PENDING")
    
    class Meta:
        model = Order
        fields= ['id','order_status', 'size', 'quantity', 'flavour']
        
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    # order_status = serializers.CharField(max_length=25)

    class Meta:
        model=Order
        fields=['order_status']