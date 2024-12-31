from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Customer, CustomerContact, CustomerNote
from .serializers import CustomerSerializer, CustomerContactSerializer, CustomerNoteSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['get'])
    def contacts(self, request, pk=None):
        customer = self.get_object()
        contacts = CustomerContact.objects.filter(customer=customer)
        serializer = CustomerContactSerializer(contacts, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def notes(self, request, pk=None):
        customer = self.get_object()
        notes = CustomerNote.objects.filter(customer=customer)
        serializer = CustomerNoteSerializer(notes, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def add_note(self, request, pk=None):
        customer = self.get_object()
        serializer = CustomerNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=customer, created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerContactViewSet(viewsets.ModelViewSet):
    queryset = CustomerContact.objects.all()
    serializer_class = CustomerContactSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        customer_id = self.request.query_params.get('customer_id', None)
        if customer_id:
            return CustomerContact.objects.filter(customer_id=customer_id)
        return CustomerContact.objects.all()

