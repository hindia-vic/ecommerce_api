from rest_framework import serializers
from . models import Orders


class OrderSerializer(serializers.ModelSerializer):
    status=serializers.HiddenField(default="PENDING")
    size=serializers.CharField(max_length=25)
    quantity=serializers.IntegerField()
    class Meta:
        model=Orders
        fields=['id','status','size','quantity']

class OrderDetailSerializer(serializers.ModelSerializer):
    size=serializers.CharField(max_length=25)
    status=serializers.CharField(default="PENDING")
    quantity=serializers.IntegerField()
    created_at=serializers.DateTimeField()
    updated_at=serializers.DateTimeField()
    class Meta:
        model=Orders
        fields=['id','status','size','quantity','created_at','updated_at']

class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    status = serializers.CharField(max_length=25)
    class Meta:
        model=Orders
        fields=['status']