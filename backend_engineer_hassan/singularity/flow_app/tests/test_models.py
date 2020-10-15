import pytest
from .factories import FlowCalculationFactory
from ..models import FlowCalculation

pytestmark = pytest.mark.django_db


class TestFlowCalculation:
    def test_ordering(self):
        objs = [FlowCalculationFactory(), FlowCalculationFactory(), FlowCalculationFactory(), FlowCalculationFactory(),
                FlowCalculationFactory(), ]
        calculations = FlowCalculation.objects.all()
        assert [calculation for calculation in calculations] == list(reversed(objs))


class TestFlowCalculationManager:
    def test_recent(self):
        objs = [FlowCalculationFactory(), FlowCalculationFactory(), FlowCalculationFactory(), FlowCalculationFactory(),
                FlowCalculationFactory(), ]
        assert FlowCalculation.objects.recent() == objs[4]
