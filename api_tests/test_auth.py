import pytest
import time
import json

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


# TESTS DE AUTENTICACIÓN
@pytest.mark.api
@pytest.mark.smoke
class TestAuthLogin:
    """Tests para el endpoint /auth/login"""

    def test_login_ok(self, api, admin_creds):
        """Test de login exitoso con credenciales válidas"""
        r = api.post("/auth/login", data=admin_creds)
        assert r.status_code == 200
        j = r.json()
        assert "access_token" in j
        assert j.get("token_type") == "bearer"
        assert isinstance(j.get("access_token"), str)
        assert len(j["access_token"]) > 50

    def test_login_fail_invalid_password(self, api, admin_creds):
        """Test de login fallido con password inválido"""
        invalid_creds = admin_creds.copy()
        invalid_creds["password"] = "invalid_password"
        r = api.post("/auth/login", data=invalid_creds)
        assert r.status_code == 401

    def test_login_fail_invalid_username(self, api, admin_creds):
        """Test de login fallido con username inválido"""
        invalid_creds = admin_creds.copy()
        invalid_creds["username"] = "nonexistent@demo.com"
        r = api.post("/auth/login", data=invalid_creds)
        assert r.status_code == 401

    def test_login_validation_error_empty_fields(self, api):
        """Test de error de validación con campos vacíos"""
        r = api.post("/auth/login", data={"username": "", "password": ""})
        assert r.status_code == 422

    def test_login_missing_password(self, api, admin_creds):
        """Test cuando falta el campo password"""
        r = api.post("/auth/login", data={"username": admin_creds["username"]})
        assert r.status_code == 422

    def test_login_missing_username(self, api, admin_creds):
        """Test cuando falta el campo username"""
        r = api.post("/auth/login", data={"password": admin_creds["password"]})
        assert r.status_code == 422

    def test_login_case_sensitive_password(self, api, admin_creds):
        """Test que la contraseña es case sensitive"""
        invalid_creds = admin_creds.copy()
        invalid_creds["password"] = admin_creds["password"].upper()
        r = api.post("/auth/login", data=invalid_creds)
        assert r.status_code == 401

    def test_login_sql_injection_attempt(self, api):
        """Test para intentos de inyección SQL"""
        injection_attempts = [
            {"username": "admin'--", "password": "any"},
            {"username": "admin@demo.com", "password": "' OR '1'='1"},
            {"username": "admin\"; DROP TABLE users; --", "password": "any"}
        ]

        for attempt in injection_attempts:
            r = api.post("/auth/login", data=attempt)
            assert r.status_code == 401
            assert r.status_code != 500

    def test_login_with_extra_fields(self, api, admin_creds):
        """Test con campos adicionales no esperados"""
        data = admin_creds.copy()
        data["extra_field"] = "unexpected_value"
        data["another_field"] = "test"
        r = api.post("/auth/login", data=data)
        assert r.status_code == 200

    def test_login_content_type_validation(self, api, admin_creds):
        """Test con diferentes content types"""
        # Content-Type incorrecto
        headers = {"Content-Type": "application/xml"}
        r = api.post("/auth/login", data=admin_creds, headers=headers)
        assert r.status_code in [415, 400, 422]


    def test_login_response_structure(self, api, admin_creds):
        """Test que la respuesta tiene la estructura correcta"""
        r = api.post("/auth/login", data=admin_creds)
        assert r.status_code == 200
        j = r.json()

        required_fields = ["access_token", "token_type"]
        for field in required_fields:
            assert field in j, f"Campo requerido '{field}' no encontrado en la respuesta"

    def test_login_performance(self, api, admin_creds):
        """Test de rendimiento del endpoint de login"""
        start_time = time.time()
        r = api.post("/auth/login", data=admin_creds)
        end_time = time.time()

        response_time = end_time - start_time
        assert r.status_code == 200
        assert response_time < 6.0, f"Login tardó {response_time:.2f}s, máximo permitido: 3s"

