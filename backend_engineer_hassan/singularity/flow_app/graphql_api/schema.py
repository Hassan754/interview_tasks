import graphene
from graphene_django.types import ObjectType

from django.core.cache import cache

from graphql import GraphQLError

from singularity.flow_app import test_sim
from singularity.flow_app.models import FlowCalculation

class ValueType(graphene.ObjectType):
    value = graphene.Float()


# Create a Query type
class Query(ObjectType):
    getActive = graphene.Field(ValueType)
    getReactive = graphene.Field(ValueType)

    def resolve_getActive(self, info, **kwargs):
        value = cache.get("active")
        if not value:
            obj = FlowCalculation.objects.recent()
            value = obj.active_power if obj else None
        if value:
            return ValueType(value=value)
        else:
            raise GraphQLError(
                'Active power is not available yet. Maybe Run calculatePower mutation ? '
            )

    def resolve_getReactive(self, info, **kwargs):
        value = cache.get("active")
        if not value:
            obj = FlowCalculation.objects.recent()
            value = obj.reactive_power if obj else None

        if value:
            return ValueType(value=value)
        else:
            raise GraphQLError(
                'Reactive power is not available yet. Maybe Run calculatePower mutation ?'
            )


class CalculatePower(graphene.Mutation):
    active = graphene.Float()
    reactive = graphene.Float()

    @staticmethod
    def mutate(root, info):
        active, reactive = test_sim.run_simulation()

        flow_calculation = FlowCalculation(active_power=active, reactive_power=reactive)
        flow_calculation.save()

        # Set Cache
        cache.set("active", active)
        cache.set("reactive", reactive)

        return CalculatePower(active=active, reactive=reactive)


class Mutation(graphene.ObjectType):
    calculate_power = CalculatePower.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
