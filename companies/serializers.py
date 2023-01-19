from rest_framework import serializers

from companies.models import Product, Company


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True,
                                              read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
