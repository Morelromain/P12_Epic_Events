from rest_framework import serializers

from .models import Client, Contract, Event


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = [
            'url', 'first_name', 'last_name', 'email', 'phone',
            'mobile', 'converted', 'date_created', 'date_update', 'sales_contact'
            ]
        read_only_fields = ['sales_contact']

    def create(self, validated_data):
        info = Client.objects.create(**validated_data)
        info.sales_contact = self.context["request"].user
        info.save()
        return info


class ContractSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'url', 'ratified', 'amount', 'payement_due',
            'date_created', 'date_update', 'sales_contact',
            'client', 'status_contract'
            ]
        read_only_fields = ['sales_contact']

    def create(self, validated_data):
        info = Contract.objects.create(**validated_data)
        info.sales_contact = self.context["request"].user
        Event.objects.create(event_contract=info, client=info.client)
        info.save()
        return info

class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = [
            'url', 'attendees', 'notes', 'date_created', 'date_update',
            'event_date', 'accomplish', 'support_contact', 'client', 'event_contract'
            ]
    read_only_fields = ['client']
    
    def create(self, validated_data):
        info = Event.objects.create(**validated_data)
        Contract.objects.filter(id=info.event_contract_id)
        info.sales_contact = self.context["request"].user
        info.save()
        return info