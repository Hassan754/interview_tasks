from django.db import models
from django.db.models.query import QuerySet

class FlowCalculationQuerySet(QuerySet):
    def recent(self):
        """Get the most recent calculation (So that the logic
        does not break In case the ordering of the model is changed)"""

        return self.order_by('-created').first()

class FlowCalculationManager(models.Manager):

    def get_query_set(self):
        return FlowCalculationQuerySet(self.model)

    def __getattr__(self, attr, *args):
        # see https://code.djangoproject.com/ticket/15062 for details
        if attr.startswith("_"):
            raise AttributeError
        return getattr(self.get_query_set(), attr, *args)
