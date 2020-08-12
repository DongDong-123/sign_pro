from django.contrib import admin

# Register your models here.
from sign.models import Event, Guest

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    search_fields = ['name']
    list_filter = ['status']

class GuestAdmin(admin.ModelAdmin):
    list_display = ['real_name', 'phone','email','sign','create_time','event']
    search_fields = ['real_name', 'phone']
    list_filter = ['sign']

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)