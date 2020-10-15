from factory.django import DjangoModelFactory

from singularity.flow_app.models import FlowCalculation


class FlowCalculationFactory(DjangoModelFactory):
    active_power = 0.1
    reactive_power = 1.2

    class Meta:
        model = FlowCalculation
