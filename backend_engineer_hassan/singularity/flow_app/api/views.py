from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from django.core.cache import cache

from django.utils.translation import gettext_lazy as _

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

        # Set Cache
        cache.set("active", active)
        cache.set("reactive", reactive)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["GET"], url_path="active", url_name="active")
    def active(self, request):
        """
        Returns the active power value from the last calculation
        """
        value = cache.get("active")
        if not value:
            obj = FlowCalculatorViewSet.get_recent_calculation()
            value = obj.active_power if obj else None

        data = {"value": value} if value else {"message": _("Active power is not available")}

        return Response(status=status.HTTP_200_OK, data=data)

    @action(detail=False, methods=["GET"], url_path="reactive", url_name="reactive")
    def reactive(self, request):
        """
        Returns the reactive power value from the last calculation
        """
        value = cache.get("reactive")
        if not value:
            obj = FlowCalculatorViewSet.get_recent_calculation()
            value = obj.reactive_power if obj else None

        data = {"value": value} if value else {"message": _("Reactive power is not available")}

        return Response(status=status.HTTP_200_OK, data=data)
