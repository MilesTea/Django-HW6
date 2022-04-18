from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_fields = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', ]
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title', 'description']
    pagination_class = LimitOffsetPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_fields = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', ]
    search_fields = ['address', 'product']
    ordering_fields = ['id', 'address', 'product']
    pagination_class = LimitOffsetPagination
