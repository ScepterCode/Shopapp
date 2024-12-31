from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# from inventory.accounts import models
# from inventory.customers import models
from .models import Category, Supplier, Product, SerialNumber, PriceHistory
from .serializers import (CategorySerializer, SupplierSerializer, ProductSerializer,
                        SerialNumberSerializer, PriceHistorySerializer)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def update_price(self, request, pk=None):
        product = self.get_object()
        new_price = request.data.get('new_price')
        reason = request.data.get('reason', '')

        if not new_price:
            return Response(
                {'error': 'New price is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        PriceHistory.objects.create(
            product=product,
            old_price=product.price,
            new_price=new_price,
            changed_by=request.user,
            reason=reason
        )

        product.price = new_price
        product.save()

        return Response({'message': 'Price updated successfully'})

    @action(detail=True, methods=['get'])
    def price_history(self, request, pk=None):
        product = self.get_object()
        history = PriceHistory.objects.filter(product=product)
        serializer = PriceHistorySerializer(history, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_serial_numbers(self, request, pk=None):
        product = self.get_object()
        serial_numbers = request.data.get('serial_numbers', [])
        
        created_serials = []
        for sn in serial_numbers:
            serial = SerialNumber.objects.create(
                product=product,
                serial_number=sn,
                status='in_stock'
            )
            created_serials.append(SerialNumberSerializer(serial).data)

        return Response(created_serials, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        products = Product.objects.filter(
            stock_quantity__lte=models.F('minimum_stock')
        )
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

class SerialNumberViewSet(viewsets.ModelViewSet):
    queryset = SerialNumber.objects.all()
    serializer_class = SerialNumberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = SerialNumber.objects.all()
        status = self.request.query_params.get('status', None)
        product_id = self.request.query_params.get('product_id', None)

        if status:
            queryset = queryset.filter(status=status)
        if product_id:
            queryset = queryset.filter(product_id=product_id)

        return queryset

