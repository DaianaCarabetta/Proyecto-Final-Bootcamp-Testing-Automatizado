import requests
import time

BASE_URL = "https://cf-automation-airline-api.onrender.com"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3ItYTRmNTBiYjgiLCJyb2xlIjoiYWRtaW4ifQ.WOYHNJ3D7bR9LJsmAtxPrsudIL-c3cIyTrJyNF7d-B0"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Lista de endpoints posibles a probar
possible_endpoints = [
    # Endpoints de auth
    "/auth/me",
    "/auth/user",
    "/auth/profile",
    "/user/me",
    "/user/profile",
    "/api/auth/me",
    "/api/v1/auth/me",

    # Endpoints de usuarios
    "/users",
    "/api/users",
    "/api/v1/users",
    "/user",
    "/api/user",

    # Endpoints de vuelos
    "/flights",
    "/api/flights",
    "/api/v1/flights",
    "/flight",

    # Endpoints de bookings
    "/bookings",
    "/api/bookings",
    "/reservations",

    # Root endpoints
    "/",
    "/api",
    "/api/v1",
    "/health",

    # Otros endpoints comunes
    "/aircrafts",
    "/api/aircrafts",
    "/airports",
    "/api/airports"
]


def discover_endpoints():
    print("🔍 Discovering actual endpoints...")
    print(f"Using token: {TOKEN[:50]}...")
    print("=" * 60)

    working_endpoints = []

    for endpoint in possible_endpoints:
        url = f"{BASE_URL}{endpoint}"

        # Probar con GET primero
        try:
            response = requests.get(url, headers=headers, timeout=5)
            status_info = f"GET {endpoint:20} -> {response.status_code} {response.reason}"

            # Si es 405, probar POST
            if response.status_code == 405:
                try:
                    response_post = requests.post(url, headers=headers, timeout=5, json={})
                    status_info += f" | POST -> {response_post.status_code} {response_post.reason}"
                except:
                    pass

            print(status_info)

            # Si es 200, guardar y mostrar info
            if response.status_code == 200:
                working_endpoints.append(endpoint)
                if response.text:
                    print(f"  Response: {response.text[:100]}...")

        except requests.exceptions.RequestException as e:
            print(f"GET {endpoint:20} -> Error: {e}")

        time.sleep(0.1)
        print()

    # Mostrar resumen
    print("=" * 60)
    print("🎯 ENDPOINTS FUNCIONANDO:")
    print("=" * 60)
    for endpoint in working_endpoints:
        print(f"✅ {endpoint}")

    if not working_endpoints:
        print("❌ No se encontraron endpoints funcionando")
        print("💡 Probablemente necesites:")
        print("   - Verificar la URL base")
        print("   - Verificar que el token sea válido")
        print("   - Revisar la documentación en /docs")


if __name__ == "__main__":
    discover_endpoints()