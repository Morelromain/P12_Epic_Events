from django.contrib import admin

from .models import Client, Contract, Event, Status

admin.site.site_header = "Epic events administration"
admin.site.site_title = "Epic events"

admin.site.register(Status)
admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
