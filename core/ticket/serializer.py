from rest_framework import serializers

from .models import Ticket, State

class TicketSerializer(serializers.ModelSerializer):
    state_str_ = serializers.CharField(read_only=True, source="state.__str__")

    class Meta:
        model = Ticket
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'