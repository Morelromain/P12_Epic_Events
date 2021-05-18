from django.db import models
from django.conf import settings


class Client(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=False)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True
        )

    def __str__(self):
        return 'Client: ' + self.last_name


class Contract(models.Model):

    contrat_status = models.BooleanField
    amount = models.FloatField
    payement_due = models.DateTimeField(auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=False)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True
        )
    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE,
        blank=True, null=True
        )


class Event(models.Model):

    attendees = models.IntegerField()
    notes = models.TextField()
    event_date = models.DateTimeField(auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=False)
    event_status = models.BooleanField
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True
        )
    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE,
        blank=True, null=True
        )
