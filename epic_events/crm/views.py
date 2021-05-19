from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import get_object_or_404

from user.models import User
from crm.models import Client, Contract, Event
from crm.serializers import ClientSerializer, ContractSerializer, EventSerializer
from .perm import ClientPermission, ContractPermission, EventPermission

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [ClientPermission & permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
            """
            Si user est un 3 (1management,2sales,3support) filtre sur ces events
            sinon affiche tous
            """
            if User.objects.filter(username=self.request.user, groups="3").exists():
                queryset = Event.objects.filter(support_contact=self.request.user)
                events = get_object_or_404(queryset)

                '''for event in events:
                    test = []
                    clients = Client.objects.filter(client_id=events.client)
                    test.append(clients)
                return clients'''
                return Client.objects.all()
            else:
                return Client.objects.all()

class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [ContractPermission & permissions.IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [EventPermission & permissions.IsAuthenticated]
    
    def get_queryset(self, *args, **kwargs):
        """
        Si user est un 3 (1management,2sales,3support) filtre sur ces events
        sinon affiche tous
        """
        if User.objects.filter(username=self.request.user, groups="3").exists():
            return Event.objects.filter(support_contact=self.request.user)
        else:
            return Event.objects.all()
