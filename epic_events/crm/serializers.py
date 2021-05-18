from rest_framework import serializers

from crm.models import Client, Contract, Event


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = [
            'first_name', 'last_name', 'email', 'phone',
            'mobile', 'sales_contact'
            ]


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'contrat_status', 'amount', 'payement_due',
            'sales_contact', 'client'
            ]


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = [
            'attendees', 'notes', 'event_status', 'event_date',
            'support_contact', 'client'
            ]
