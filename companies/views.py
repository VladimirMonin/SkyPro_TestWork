from rest_framework import viewsets
from companies.models import Product
from companies.serializers import ProductSerializer, CompanySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CompanySerializer
