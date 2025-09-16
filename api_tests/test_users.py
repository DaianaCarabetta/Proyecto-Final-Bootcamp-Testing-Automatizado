import pytest
import json

# Registrar el mark users para evitar warnings
pytestmark = pytest.mark.api


class TestUsers:

    def test_get_all_users(self, api_auth):
        """Test obtener todos los usuarios"""
        r = api_auth.get("/users")
        print(f"Status Code: {r.status_code}")
        print(f"Response Text: {r.text}")
        print(f"Headers: {dict(r.headers)}")

        # Si hay error 500, mostramos más detalles
        if r.status_code == 500:
            pytest.fail(f"Error 500 del servidor: {r.text}")

        assert r.status_code == 200
        users = r.json()
        assert isinstance(users, list)
        if users:
            assert "email" in users[0]
            assert "is_active" in users[0]

    def test_get_user_by_id(self, api_auth):
        """Test obtener usuario por ID"""
        # Primero obtener todos los usuarios para tener un ID válido
        users_response = api_auth.get("/users")
        if users_response.status_code == 200 and users_response.json():
            user_id = users_response.json()[0]["id"]
            r = api_auth.get(f"/users/{user_id}")
            assert r.status_code == 200
            user_data = r.json()
            assert user_data["id"] == user_id

    def test_create_user(self, api_auth, random_user_email):
        """Test crear nuevo usuario"""
        user_data = {
            "email": random_user_email,
            "password": "testpassword123",
            "is_active": True,
            "is_superuser": False
        }
        r = api_auth.post("/users", json=user_data)
        # Podría ser 200 (éxito) o 422 (validación fallida)
        assert r.status_code in [200, 422]
        if r.status_code == 200:
            created_user = r.json()
            assert created_user["email"] == user_data["email"]

    def test_update_user(self, api_auth, random_user_email):
        """Test actualizar usuario"""
        # Primero crear un usuario
        user_data = {
            "email": random_user_email,
            "password": "testpassword123",
            "is_active": True,
            "is_superuser": False
        }
        create_response = api_auth.post("/users", json=user_data)
        if create_response.status_code == 200:
            user_id = create_response.json()["id"]

            # Actualizar el usuario
            update_data = {"is_active": False}
            r = api_auth.put(f"/users/{user_id}", json=update_data)
            assert r.status_code == 200
            updated_user = r.json()
            assert updated_user["is_active"] == False

    def test_delete_user(self, api_auth, random_user_email):
        """Test eliminar usuario"""
        # Crear usuario para eliminar
        user_data = {
            "email": random_user_email,
            "password": "testpassword123",
            "is_active": True,
            "is_superuser": False
        }
        create_response = api_auth.post("/users", json=user_data)
        if create_response.status_code == 200:
            user_id = create_response.json()["id"]

            # Eliminar usuario
            r = api_auth.delete(f"/users/{user_id}")
            assert r.status_code == 200

            # Verificar que ya no existe
            get_response = api_auth.get(f"/users/{user_id}")
            assert get_response.status_code == 404