# api_tests/conftest.py
import os
from pathlib import Path
import pytest
import requests
from dotenv import load_dotenv

# Cargar .env desde la raíz del repo
ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

BASE_URL = (os.getenv("BASE_URL") or "https://cf-automation-airline-api.onrender.com").rstrip("/")

class API:
    def __init__(self, base): self.base = base.rstrip("/")
    def _u(self, p): return self.base + (p if p.startswith("/") else "/" + p)
    def get(self, p, **kw):    return requests.get(self._u(p), timeout=20, **kw)
    def post(self, p, **kw):   return requests.post(self._u(p), timeout=20, **kw)
    def put(self, p, **kw):    return requests.put(self._u(p), timeout=20, **kw)
    def delete(self, p, **kw): return requests.delete(self._u(p), timeout=20, **kw)

@pytest.fixture
def api() -> API:
    assert BASE_URL, "Falta BASE_URL en .env"
    return API(BASE_URL)

# --- agregar en api_tests/conftest.py ---

import uuid

def random_email(domain="example.com")->str:
    return f"usr-{uuid.uuid4().hex[:8]}@{domain}"

@pytest.fixture(scope="session")
def admin_creds():
    return {
        "username": os.getenv("ADMIN_USER", "admin@demo.com"),
        "password": os.getenv("ADMIN_PASS", "admin123"),
    }

@pytest.fixture(scope="session")
def token(api, admin_creds)->str:
    # OAuth2 password flow
    r = api.post("/auth/login", data=admin_creds)
    assert r.status_code == 200, f"Login falló: {r.status_code} {r.text}"
    body = r.json()
    assert body.get("access_token") and body.get("token_type") == "bearer"
    return body["access_token"]

@pytest.fixture
def api_auth(token):
    # API client con Bearer token
    class APIAuth(type(api())):  # reutiliza la clase API de tu conftest
        pass
    client = api()
    client.s.headers.update({"Authorization": f"Bearer {token}"})
    return client
