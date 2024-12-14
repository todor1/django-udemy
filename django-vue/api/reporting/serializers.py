from rest_framework import serializers
from reporting.models import Customer, Order, Product, Supplier, Category

""" 
    The order of classes here is not significant as in the models.py file.
    Serializers are on a higher level of abstraction than models.
    Serializers are used to convert complex data types, such as querysets and model instances, 
    to native Python datatypes that can then be easily rendered into JSON, XML, or other content types.
"""


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        # fields = [
        #     "id",
        #     "first_name",
        #     "last_name",
        #     "gender",
        #     "title",
        #     "address",
        #     "city",
        #     "region",
        #     "postal_code",
        #     "country",
        #     "phone",
        #     "email",
        # ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "supplier",
            "category",
            "unit_price",
            "units_in_stock",
            "units_on_order",
        ]

    def to_representation(self, instance):
        self.fields["supplier"] = SupplierSerializer(read_only=True)
        self.fields["category"] = CategorySerializer(read_only=True)
        return super(ProductSerializer, self).to_representation(instance)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["customer"] = CustomerSerializer(read_only=True)
        self.fields["product"] = ProductSerializer(read_only=True)
        return super(OrderSerializer, self).to_representation(instance)
