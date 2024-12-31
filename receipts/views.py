from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Receipt
from .serializers import ReceiptSerializer

@api_view(['GET', 'POST'])
def receipt_list(request):
    if request.method == 'GET':
        receipts = Receipt.objects.all()
        serializer = ReceiptSerializer(receipts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)

    if request.method == 'GET':
        serializer = ReceiptSerializer(receipt)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReceiptSerializer(receipt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        receipt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

