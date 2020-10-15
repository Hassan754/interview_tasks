import pytest
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def api_client():
    def inner(user=None, *args, **kwargs):
        ac = APIClient(*args, **kwargs)
        if user is not None:
            ac.force_authenticate(user)
        return ac

    return inner
