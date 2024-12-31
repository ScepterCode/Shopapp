from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Quotation, QuotationItem
from .serializers import QuotationSerializer, QuotationItemSerializer

# View for listing and creating quotations
@api_view(['GET', 'POST'])
def quotation_list(request):
    if request.method == 'GET':
        quotations = Quotation.objects.all()  # Fetch all quotations
        serializer = QuotationSerializer(quotations, many=True)  # Serialize data
        return Response(serializer.data)  # Return serialized data

    elif request.method == 'POST':
        serializer = QuotationSerializer(data=request.data)  # Deserialize incoming data
        if serializer.is_valid():
            serializer.save()  # Save if valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with created data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Respond with validation errors

# View for retrieving, updating, or deleting a specific quotation
@api_view(['GET', 'PUT', 'DELETE'])
def quotation_detail(request, pk):
    quotation = get_object_or_404(Quotation, pk=pk)  # Fetch the quotation or return 404

    if request.method == 'GET':
        serializer = QuotationSerializer(quotation)  # Serialize data
        return Response(serializer.data)  # Return serialized data

    elif request.method == 'PUT':
        serializer = QuotationSerializer(quotation, data=request.data)  # Deserialize and validate data
        if serializer.is_valid():
            serializer.save()  # Save updates if valid
            return Response(serializer.data)  # Respond with updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Respond with validation errors

    elif request.method == 'DELETE':
        quotation.delete()  # Delete the quotation
        return Response(status=status.HTTP_204_NO_CONTENT)  # Respond with no content

# View for adding an item to a specific quotation
@api_view(['POST'])
def add_quotation_item(request, pk):
    quotation = get_object_or_404(Quotation, pk=pk)  # Fetch the quotation or return 404
    serializer = QuotationItemSerializer(data=request.data)  # Deserialize incoming data
    if serializer.is_valid():
        serializer.save(quotation=quotation)  # Save the item linked to the quotation
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Respond with created data
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Respond with validation errors

