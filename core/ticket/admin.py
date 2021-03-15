# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Ticket, State

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    fields_ticket = ["id", "title", "state", "created_at"]
    list_display = fields_ticket
    search_fields = fields_ticket
    list_filter = fields_ticket
    readonly_fields = ('created_at',)
    ordering = ['created_at']

class StateAdmin(admin.ModelAdmin):

    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    ordering = ['name']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(State, StateAdmin)