# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Ticket(models.Model):
    STATE_CHOICES = (
        ('1', 'Abierto'),
        ('2', 'Pendiente'),
        ('3', 'En Proceso'),
        ('4', 'Resuelto'),
        ('5', 'Cerrado'),
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    state = models.CharField(max_length=200, choices = STATE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
