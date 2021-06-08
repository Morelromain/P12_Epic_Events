from django.db import models
from django.conf import settings


class Status(models.Model):

    label = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return 'N° ' + str(self.id) + ' ' + self.label

    class Meta:
        ordering = ['id']


class Client(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=25, blank=True, null=True)
    mobile = models.CharField(max_length=25, blank=True, null=True)
    converted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        ordering = ['-date_update']


class Contract(models.Model):

    ratified = models.BooleanField(default=False)
    amount = models.FloatField(null=True)
    payement_due = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True)
    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE)
    status_contract = models.ForeignKey(
        to=Status, on_delete=models.CASCADE,
        blank=True, null=True)

    def __str__(self):
        return 'N° ' + str(self.id) + ' ' + str(self.client)

    class Meta:
        ordering = ['-date_update']


class Event(models.Model):

    attendees = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    accomplish = models.BooleanField(default=False)
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True)
    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE,
        blank=True, null=True)
    event_contract = models.OneToOneField(
        to=Contract,
        on_delete=models.CASCADE)

    def __str__(self):
        return 'N° ' + str(self.id) + ' ' + str(self.client)

    class Meta:
        ordering = ['-date_update']
