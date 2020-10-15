import pytest
from django.urls import reverse


pytestmark = pytest.mark.django_db


def test_flow_calculation_active():
    assert (
        reverse("api:flow_app:flow-active")
        == f"/api/flow/active/"
    )


def test_flow_calculation_reactive():
    assert (
        reverse("api:flow_app:flow-reactive")
        == f"/api/flow/reactive/"
    )


def test_flow_calculation_list():
    assert (
        reverse("api:flow_app:flow-list")
        == f"/api/flow/"
    )
