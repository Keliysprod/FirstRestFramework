from django.contrib import admin
from .models import CustomUser, Event, Invited

admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(Invited)