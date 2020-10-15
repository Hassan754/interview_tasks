import pytest
from django.core.cache import cache
from rest_framework import status
from rest_framework.reverse import reverse

from ..api.views import FlowCalculatorViewSet
from .factories import FlowCalculationFactory
from ..models import FlowCalculation

pytestmark = pytest.mark.django_db


class TestFlowViewSet:

    def test_get_recent_calculation(self, django_assert_num_queries):
        obj1 = FlowCalculationFactory.create()
        obj2 = FlowCalculationFactory.create()
        obj3 = FlowCalculationFactory.create()

        with django_assert_num_queries(1):
            target = FlowCalculatorViewSet.get_recent_calculation()

        assert target.id == obj3.id

    def test_flow_active(self, api_client, django_assert_num_queries):
        url_name = "api:flow_app:flow-active"

        obj1 = FlowCalculationFactory.create()

        with django_assert_num_queries(3):
            response = api_client().get(reverse(url_name))

        assert response.status_code == status.HTTP_200_OK
        assert obj1.active_power == response.data['value']

    def test_flow_reactive(self, api_client, django_assert_num_queries):
        url_name = "api:flow_app:flow-reactive"

        obj1 = FlowCalculationFactory.create()

        with django_assert_num_queries(3):
            response = api_client().get(reverse(url_name))

        assert response.status_code == status.HTTP_200_OK
        assert obj1.reactive_power == response.data['value']

    def test_flow_create(self, api_client, django_assert_num_queries):
        url_name = "api:flow_app:flow-list"

        assert FlowCalculation.objects.count() == 0
        with django_assert_num_queries(3):
            response = api_client().post(reverse(url_name))
        assert FlowCalculation.objects.count() == 1
        assert response.status_code == status.HTTP_201_CREATED

        assert cache.get("active") is not None
