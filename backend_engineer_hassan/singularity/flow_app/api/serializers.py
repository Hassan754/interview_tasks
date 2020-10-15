from rest_framework import serializers

from singularity.flow_app.models import FlowCalculation


class FlowCalculationSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlowCalculation
        fields = ('active_power','reactive_power','created')
        read_only_fields = ('created',)

