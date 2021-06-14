from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, Contract, Event, Status
from .serializers import (
    ClientSerializer, ContractSerializer,
    EventSerializer, StatusSerializer)
from .perm import (
    ClientPermission, ContractPermission,
    EventPermission, StatusPermission)


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

    @action(detail=False, methods=['GET'])
    def my_own_clients(self, request, **kwargs):
        queryset = self.get_queryset().filter(sales_contact=self.request.user)
        serializer = ClientSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Contracts to be viewed or edited.
    """

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [(ContractPermission & permissions.IsAuthenticated)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['ratified', 'amount', 'payement_due', 'client']

    @action(detail=False, methods=['GET'])
    def my_own_contracts(self, request, **kwargs):
        queryset = self.get_queryset().filter(sales_contact=self.request.user)
        serializer = ContractSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


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

    @action(detail=False, methods=['GET'])
    def my_own_events(self, request, **kwargs):
        queryset = self.get_queryset().filter(support_contact=self.request.user)
        serializer = EventSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Status to be viewed.
    """

    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [(StatusPermission & permissions.IsAuthenticated)]
