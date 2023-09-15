from rest_framework import serializers
from shop.models import Product

class ProductSerializer(serializers.ModelSerializer):
#                       객체 직렬화
#                       object Serialization
#       논리적인 객체     =>      직렬화     =>      객체

    class Meta:
        model = Product
        fields = ('product_code', 'product_name', 'price', 'description', 'filename')