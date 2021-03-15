# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class State(models.Model):
    name = models.CharField(max_length=20, verbose_name="Estado")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

class Ticket(models.Model):

    title = models.CharField(max_length=30, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado en")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"


