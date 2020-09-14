from rest_framework import serializers
from app1.models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    def validate_quantity(self,quantity):
        if quantity>=1:
            return quantity
        else:
            raise serializers.ValidationError("Quantity should be greater than 1 or equal to one")

    class Meta:
        fields = "__all__"
        model = ProductModel
