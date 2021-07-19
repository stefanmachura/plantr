import pytest

from django.contrib.auth import get_user_model

sample_user_data = {"email": "test@test.com", "password": "pass"}


@pytest.fixture
def sample_user():
    user = get_user_model()
    u, _ = user.objects.get_or_create(**sample_user_data)
    return u
