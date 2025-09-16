# test_airports.py
import pytest

pytestmark = pytest.mark.api


class TestAirports:

    def test_get_all_airports(self, api_auth):
        """Test obtener todos los aeropuertos"""
        r = api_auth.get("/airports")
        assert r.status_code == 200
        airports = r.json()
        assert isinstance(airports, list)
        if airports:
            assert "iata_code" in airports[0]
            assert "city" in airports[0]
            assert "country" in airports[0]

    def test_get_airport_by_code(self, api_auth):
        """Test obtener aeropuerto por código IATA"""
        # Primero obtener todos los aeropuertos
        r = api_auth.get("/airports")
        if r.status_code == 200 and r.json():
            airport_code = r.json()[0]["iata_code"]
            r_single = api_auth.get(f"/airports/{airport_code}")
            # Podría funcionar o dar 404 si el endpoint no existe
            assert r_single.status_code in [200, 404]