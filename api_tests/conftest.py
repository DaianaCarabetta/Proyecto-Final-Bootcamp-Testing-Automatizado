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
