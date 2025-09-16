# api_tests/conftest.py
import os
from pathlib import Path
import pytest
import requests
from dotenv import load_dotenv
import uuid

# Cargar .env desde la raíz del repo
ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

BASE_URL = (os.getenv("BASE_URL") or "https://cf-automation-airline-api.onrender.com").rstrip("/")


class API:
    def __init__(self, base):
        self.base = base.rstrip("/")
        self.session = requests.Session()

    def _u(self, p):
        return self.base + (p if p.startswith("/") else "/" + p)

    def get(self, p, **kw):
        return self.session.get(self._u(p), timeout=20, **kw)

    def post(self, p, **kw):
        return self.session.post(self._u(p), timeout=20, **kw)

    def put(self, p, **kw):
        return self.session.put(self._u(p), timeout=20, **kw)

    def delete(self, p, **kw):
        return self.session.delete(self._u(p), timeout=20, **kw)


# Fixture con scope session para reutilizar la conexión
@pytest.fixture(scope="session")
def api() -> API:
    assert BASE_URL, "Falta BASE_URL en .env"
    return API(BASE_URL)


def random_email(domain="example.com") -> str:
    return f"usr-{uuid.uuid4().hex[:8]}@{domain}"


@pytest.fixture(scope="session")
def admin_creds():
    return {
        "username": os.getenv("ADMIN_USER", "admin@demo.com"),
        "password": os.getenv("ADMIN_PASS", "admin123"),
    }


# Cambiar token a fixture de función en lugar de session
@pytest.fixture
def token(api, admin_creds) -> str:
    """Fixture para obtener token de autenticación (scope function)"""
    # OAuth2 password flow
    r = api.post("/auth/login", data=admin_creds)
    assert r.status_code == 200, f"Login falló: {r.status_code} {r.text}"
    body = r.json()
    assert body.get("access_token") and body.get("token_type") == "bearer"
    return body["access_token"]


@pytest.fixture
def api_auth(api, token):
    """API client con Bearer token (scope function)"""
    # Crear una nueva instancia para no modificar la original
    auth_api = API(BASE_URL)
    auth_api.session.headers.update({"Authorization": f"Bearer {token}"})
    return auth_api


# Fixtures adicionales para testing
@pytest.fixture
def random_user_email():
    return random_email()


@pytest.fixture
def test_flight_data():
    from datetime import datetime, timedelta
    return {
        "flight_number": f"TEST{uuid.uuid4().hex[:4]}",
        "origin": "JFK",
        "destination": "LAX",
        "departure_time": (datetime.now() + timedelta(hours=2)).isoformat(),
        "arrival_time": (datetime.now() + timedelta(hours=5)).isoformat(),
        "total_seats": 150,
        "available_seats": 150,
        "price": 299.99
    }