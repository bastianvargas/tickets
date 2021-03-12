# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Ticket

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ["title", "state", "created_at"]


admin.site.register(Ticket, TicketAdmin)