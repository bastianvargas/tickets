from django.conf.urls import url, include
from rest_framework import routers

from .viewsets import TicketViewSet, StateViewSet

route = routers.SimpleRouter()
route.register('ticket', TicketViewSet)
route.register('state', StateViewSet)

urlpatterns = route.urls