# api_tests/test_health.py
import pytest

@pytest.mark.api
def test_root_health(api):
    r = api.get("/")
    assert r.status_code == 200
    assert r.json().get("msg")
