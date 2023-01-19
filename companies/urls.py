from django.urls import path, include
from rest_framework.routers import DefaultRouter

from companies.views import CompanyViewSet, ProductViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet, basename='companies')
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]
