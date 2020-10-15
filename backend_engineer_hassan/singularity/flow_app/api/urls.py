from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

from .views import (
    FlowCalculatorViewSet
)

router.register("", FlowCalculatorViewSet, "flow")

app_name = "flow_app"

urlpatterns = []

urlpatterns += router.urls
