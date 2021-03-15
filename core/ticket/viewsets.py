from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models import Ticket, State
from .serializer import TicketSerializer, StateSerializer

class TicketViewSet(viewsets.ModelViewSet):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    # def get_permissions(self):
    #     if self.action == 'create':
    #         permission_classes = [IsAdminUser]
    #     else :
    #         permission_classes = [IsAuthenticatedOrReadOnly]
    #     return [permission() for permission in permission_classes]



class StateViewSet(viewsets.ModelViewSet):

    queryset = State.objects.all()
    serializer_class = StateSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        else :
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]