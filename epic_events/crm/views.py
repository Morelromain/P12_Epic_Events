from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .perm import ClientPermission, ContractPermission, EventPermission


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Clients to be viewed or edited.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [(ClientPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = [
        'first_name', 'last_name', 'email', 'phone',
        'mobile', 'converted', 'sales_contact']
    search_fields = ['first_name', 'last_name']


class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Contracts to be viewed or edited.
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [(ContractPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['ratified', 'amount', 'payement_due', 'client']


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Events to be viewed or edited.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [(EventPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = [
        'attendees', 'event_date', 'accomplish',
        'support_contact', 'event_contract', 'client']
    search_fields = ['notes']


class MyClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the user's Clients to be viewed or edited.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [(ClientPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = [
        'first_name', 'last_name', 'email', 'phone',
        'mobile', 'converted', 'sales_contact']
    search_fields = ['first_name', 'last_name']

    def get_queryset(self):
        user = self.request.user
        return Client.objects.filter(sales_contact=user)


class MyContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the user's Contracts to be viewed or edited.
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [(ContractPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['ratified', 'amount', 'payement_due', 'client']

    def get_queryset(self):
        user = self.request.user
        return Contract.objects.filter(sales_contact=user)


class MyEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows the user's Events to be viewed or edited.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [(EventPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = [
        'attendees', 'event_date', 'accomplish',
        'support_contact', 'event_contract', 'client']
    search_fields = ['notes']

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(support_contact=user)
