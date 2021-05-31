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
    permission_classes = [(ClientPermission & permissions.IsAuthenticated) | permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['first_name', 'last_name', 'converted', 'sales_contact']
    search_fields = ['first_name', 'last_name', 'email', 'phone',
            'mobile', 'sales_contact']

    def get_queryset(self, *args, **kwargs):
            """
            Si user est un 3 (2management,1sales,3support) filtre sur ces events
            sinon affiche tous
            """
            if User.objects.filter(username=self.request.user, groups="3").exists():
                '''queryset = Event.objects.filter(support_contact=self.request.user)
                """events = get_object_or_404(queryset)"""
                test = []
                for event in queryset:
                    aaa = get_object_or_404(queryset)
                    print(aaa.client_id)
                    clients = Client.objects.filter(id=aaa.client_id)
                    test.append(clients)
                return test'''
                return Client.objects.all()
            else:
                return Client.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [(ContractPermission & permissions.IsAuthenticated) | permissions.IsAdminUser]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [(EventPermission & permissions.IsAuthenticated) | permissions.IsAdminUser]
    
    '''def get_queryset(self, *args, **kwargs):
        """
        Si user est un 3 (1management,2sales,3support) filtre sur ces events
        sinon affiche tous
        """
        if User.objects.filter(username=self.request.user, groups="3").exists():
            return Event.objects.filter(support_contact=self.request.user)
        else:
            return Event.objects.all()'''
