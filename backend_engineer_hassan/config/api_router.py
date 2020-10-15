from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

import singularity.flow_app.api.urls as flow_urls
if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = "api"

urlpatterns = [
    path('flow/', include((flow_urls, 'flow_app'))),
]
urlpatterns += router.urls
