from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FlowAppConfig(AppConfig):
    name = "singularity.flow_app"
    verbose_name = _("FlowApp")

    def ready(self):
        try:
            import singularity.flow_app.signals  # noqa F401
        except ImportError:
            pass
