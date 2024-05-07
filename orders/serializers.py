from rest_framework import serializers
from .models import Order, OrderItem
from decimal import Decimal

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'products', 'total_price', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total_price = Decimal(0.00)
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price
            total = price * quantity
            OrderItem.objects.create(order=order, **item_data)

            total_price += total
        order.total_price = total_price
        order.save()
        return order
