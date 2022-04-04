from .models import User
from rest_framework import serializers,status
from rest_framework.validators import ValidationError

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'