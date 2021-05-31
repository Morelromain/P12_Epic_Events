from rest_framework import serializers

from crm.models import Client, Contract, Event


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = [
            'url', 'first_name', 'last_name', 'email', 'phone',
            'mobile', 'converted', 'date_created', 'date_update', 'sales_contact'
            ]

class ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'url', 'ratified', 'amount', 'payement_due',
            'date_created', 'date_update', 'sales_contact', 'client'
            ]
        '''extra_kwargs = {
        "url": {"view_name": "api:aaa"}
        }'''

class EventSerializer(serializers.HyperlinkedModelSerializer):
    '''event_contract = serializers.HyperlinkedRelatedField(view_name='api:aaa', read_only=True)'''
    class Meta:
        model = Event
        fields = [
            'url', 'attendees', 'notes', 'date_created', 'date_update',
            'event_date', 'accomplish', 'support_contact', 'client', 'event_contract'
            ]
