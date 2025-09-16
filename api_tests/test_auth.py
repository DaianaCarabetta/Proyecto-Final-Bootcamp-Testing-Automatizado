import pytest

@pytest.mark.api
@pytest.mark.smoke
def test_login_ok(api, admin_creds):
    r = api.post("/auth/login", data=admin_creds)
    assert r.status_code == 200
    j = r.json()
    assert j.get("access_token")
    assert j.get("token_type") == "bearer"

@pytest.mark.api
def test_login_fail_invalid_credentials(api):
    r = api.post("/auth/login", data={"username":"admin@demo.com","password":"malapass"})
    assert r.status_code == 401

@pytest.mark.api
def test_login_validation_error(api):
    r = api.post("/auth/login", data={"username":"", "password":""})
    assert r.status_code == 422
