from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Client, Contract, Event

admin.site.site_header = "Epic events administration"
admin.site.site_title = "Epic events"

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
