from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .. import test_sim
from ..models import FlowCalculation

from ..api.serializers import FlowCalculationSerializer

User = get_user_model()


class FlowCalculatorViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = FlowCalculationSerializer
    queryset = FlowCalculation.objects.all()

    @staticmethod
    def get_recent_calculation():
        return FlowCalculation.objects.recent()

    def create(self, request, *args, **kwargs):
        """
        Do the power calculation and return the result after storing it in db
        """
        active, reactive = test_sim.run_simulation()
        serializer = self.get_serializer(data={"active_power": active, "reactive_power": reactive})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["GET"], url_path="active", url_name="active")
    def active(self, request):
        """
        Returns the active power value from the last calculation
        """
        obj = FlowCalculatorViewSet.get_recent_calculation()
        return Response(status=status.HTTP_200_OK, data={"active_power": obj.active_power})

    @action(detail=False, methods=["GET"], url_path="reactive", url_name="reactive")
    def reactive(self, request):
        """
        Returns the reactive power value from the last calculation
        """
        obj = FlowCalculatorViewSet.get_recent_calculation()
        return Response(status=status.HTTP_200_OK, data={"reactive_power": obj.reactive_power})
