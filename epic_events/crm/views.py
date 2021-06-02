from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from user.models import User
from crm.models import Client, Contract, Event
from crm.serializers import ClientSerializer, ContractSerializer, EventSerializer
from .perm import ClientPermission, ContractPermission, EventPermission


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [(ClientPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['first_name', 'last_name', 'email', 'phone',
            'mobile', 'converted', 'sales_contact']
    search_fields = ['first_name', 'last_name']


class MyClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [(ClientPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['first_name', 'last_name', 'email', 'phone',
            'mobile', 'converted', 'sales_contact']
    search_fields = ['first_name', 'last_name']
    
    def get_queryset(self):
        """
        This view should return a list of all the client
        for the currently authenticated user.
        """
        user = self.request.user
        return Client.objects.filter(sales_contact=user)


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [(ContractPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['ratified', 'amount', 'payement_due', 'client']


class MyContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [(ContractPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['ratified', 'amount', 'payement_due', 'client']
    
    def get_queryset(self):
        """
        This view should return a list of all the contract
        for the currently authenticated user.
        """
        user = self.request.user
        return Contract.objects.filter(sales_contact=user)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [(EventPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['attendees', 'event_date', 'accomplish', 'support_contact', 'event_contract', 'client',]
    search_fields = ['notes']


class MyEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [(EventPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['attendees', 'event_date', 'accomplish', 'support_contact', 'event_contract', 'client',]
    search_fields = ['notes']
    
    def get_queryset(self):
        """
        This view should return a list of all the event
        for the currently authenticated user.
        """
        user = self.request.user
        return Event.objects.filter(support_contact=user)