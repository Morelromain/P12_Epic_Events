from rest_framework import serializers

from .models import Client, Contract, Event, Status


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = [
            'url', 'first_name', 'last_name', 'email', 'phone',
            'mobile', 'converted', 'date_created', 'date_update',
            'sales_contact']
        read_only_fields = ['sales_contact']

    def create(self, validated_data):
        """
        Create a client: 
        - field sales_contact is the creator
        """

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
            'client', 'status_contract']
        read_only_fields = ['sales_contact']

    def create(self, validated_data):
        """
        Create a contract: 
        - field sales_contact is the creator
        - the field converted connected client changes to true
        - create automatically a Event with some Contract info
        """

        info = Contract.objects.create(**validated_data)
        info.sales_contact = self.context["request"].user
        Event.objects.create(event_contract=info, client=info.client)
        client = Client.objects.get(id=info.client_id)
        client.converted = True
        client.save()
        info.save()
        return info


class EventSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Event
        fields = [
            'url', 'attendees', 'notes', 'date_created', 'date_update',
            'event_date', 'accomplish', 'support_contact', 'client',
            'event_contract']
    read_only_fields = ['client']


class StatusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Status
        fields = [
            'url', 'label', 'notes']
        read_only_fields = ['label', 'notes']
