from django.db.models import FloatField
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel  # Created and modified DateTimeFields

from singularity.flow_app.managers import FlowCalculationManager


class FlowCalculation(TimeStampedModel):
    """Log of the executed power flow calculations."""

    active_power = FloatField(_("Active Power Value"))
    reactive_power = FloatField(_("Reactive Power Value"))

    objects = FlowCalculationManager()

    class Meta:
        ordering = ("-created",)
