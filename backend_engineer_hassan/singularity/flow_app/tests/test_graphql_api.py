import pytest
from graphene.test import Client
from graphql import GraphQLError

from .factories import FlowCalculationFactory
from ..graphql_api.schema import schema

pytestmark = pytest.mark.django_db


class TestPowerSchema:
    @property
    def api_client(self):
        return Client(schema)

    def test_calculate_query(self):
        mutations_calculate_power = """
            mutation {
              calculatePower {
                active
                reactive
              }
            }
        """
        response = self.api_client.execute(mutations_calculate_power)
        response_data = response.get('data').get('calculatePower')

        assert response_data['active']
        assert response_data['reactive']


    def test_get_active(self):
        get_active_query = """
        query {
            getActive {
                value
            }
        }
        """
        calculation = FlowCalculationFactory()

        response = self.api_client.execute(get_active_query)
        response_data = response.get('data').get('getActive')
        assert response_data['value']

    def test_get_reactive(self):
        get_reactive_query = """
        query {
            getReactive {
                value
            }
        }
        """
        calculation = FlowCalculationFactory()

        response = self.api_client.execute(get_reactive_query)
        response_data = response.get('data').get('getReactive')
        assert response_data['value']
