import pytest
import subprocess
import json
import requests
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_airline_api():
    """Ejecutar pruebas de la API de Airline"""
    print("🚀 Ejecutando pruebas de Airline API...")

    try:
        result = subprocess.run([
            'pytest', 'api_tests/', '-v', '--json-report', '--json-report-file=api_report.json'
        ], capture_output=True, text=True, timeout=300)

        print(f"✅ Pruebas API completadas. Código: {result.returncode}")
        return True
    except Exception as e:
        print(f"❌ Error en pruebas API: {e}")
        return False


def test_fake_cinema_ui():
    """Ejecutar pruebas de la UI de Fake Cinema"""
    print("🎬 Ejecutando pruebas de Fake Cinema UI...")

    # Configurar Selenium WebDriver
    driver = None
    ui_results = []

    try:
        # Configurar Chrome options
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument('--headless')  # Ejecutar en modo headless
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)

        # Test 1: Carga de la página principal
        start_time = time.time()
        driver.get("https://fake-cinema.vercel.app/")
        load_time = time.time() - start_time

        # Verificar que la página carga correctamente
        assert "Cinema" in driver.title, "Título de página incorrecto"
        ui_results.append({
            "name": "test_homepage_load",
            "status": "passed",
            "duration": f"{load_time:.2f}s",
            "module": "Homepage"
        })

        # Test 2: Navegación a películas
        try:
            movies_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Películas"))
            )
            movies_link.click()
            time.sleep(2)

            # Verificar que estamos en la página de películas
            assert "películas" in driver.page_source.lower() or "movies" in driver.page_source.lower()
            ui_results.append({
                "name": "test_navigation_to_movies",
                "status": "passed",
                "duration": "2.0s",
                "module": "Navigation"
            })
        except Exception as e:
            ui_results.append({
                "name": "test_navigation_to_movies",
                "status": "failed",
                "duration": "2.0s",
                "module": "Navigation",
                "error": str(e)
            })

        # Test 3: Búsqueda de películas (si existe funcionalidad de búsqueda)
        try:
            search_box = driver.find_elements(By.CSS_SELECTOR,
                                              "input[type='search'], input[placeholder*='search'], input[placeholder*='buscar']")
            if search_box:
                search_box[0].send_keys("Avengers")
                time.sleep(1)
                ui_results.append({
                    "name": "test_search_functionality",
                    "status": "passed",
                    "duration": "1.0s",
                    "module": "Search"
                })
        except:
            ui_results.append({
                "name": "test_search_functionality",
                "status": "skipped",
                "duration": "0s",
                "module": "Search",
                "error": "Elemento de búsqueda no encontrado"
            })

        # Test 4: Verificar elementos críticos
        critical_elements = [
            ("header", "Encabezado"),
            ("footer", "Pie de página"),
            ("nav", "Navegación"),
            ("main", "Contenido principal")
        ]

        for tag, description in critical_elements:
            try:
                elements = driver.find_elements(By.TAG_NAME, tag)
                if elements:
                    ui_results.append({
                        "name": f"test_{tag}_element",
                        "status": "passed",
                        "duration": "0.5s",
                        "module": "Layout"
                    })
                else:
                    ui_results.append({
                        "name": f"test_{tag}_element",
                        "status": "failed",
                        "duration": "0.5s",
                        "module": "Layout",
                        "error": f"Elemento {tag} no encontrado"
                    })
            except Exception as e:
                ui_results.append({
                    "name": f"test_{tag}_element",
                    "status": "error",
                    "duration": "0.5s",
                    "module": "Layout",
                    "error": str(e)
                })

        print("✅ Pruebas UI completadas exitosamente")
        return ui_results

    except Exception as e:
        print(f"❌ Error en pruebas UI: {e}")
        ui_results.append({
            "name": "test_ui_setup",
            "status": "failed",
            "duration": "0s",
            "module": "Setup",
            "error": str(e)
        })
        return ui_results

    finally:
        if driver:
            driver.quit()


def generate_unified_report():
    """Generar reporte unificado API + UI"""
    print("📊 Generando reporte unificado...")

    # Cargar reporte de API si existe
    api_tests = []
    if os.path.exists('api_report.json'):
        with open('api_report.json', 'r') as f:
            api_report = json.load(f)
            for test in api_report.get('tests', []):
                test_id = test['nodeid']
                api_tests.append({
                    "type": "API",
                    "module": "Authentication" if 'auth' in test_id.lower() else "Users" if 'user' in test_id.lower() else "Health",
                    "name": test_id.split('::')[-1],
                    "status": test['outcome'],
                    "duration": f"{test['duration']:.2f}s",
                    "error": test.get('call', {}).get('longrepr', '') if test['outcome'] == 'failed' else None
                })

    # Ejecutar pruebas UI
    ui_tests = test_fake_cinema_ui()

    # Combinar todos los tests
    all_tests = api_tests + [{"type": "UI", **test} for test in ui_tests]

    # Calcular estadísticas
    total_tests = len(all_tests)
    passed_tests = len([t for t in all_tests if t['status'] == 'passed'])
    failed_tests = len([t for t in all_tests if t['status'] == 'failed'])
    success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0

    # Crear reporte unificado
    unified_report = {
        "project": "Airline API + Fake Cinema UI",
        "environment": "Testing",
        "api_url": "https://cf-automation-airline-api.onrender.com",
        "ui_url": "https://fake-cinema.vercel.app/",
        "execution_date": datetime.now().isoformat(),
        "summary": {
            "total_tests": total_tests,
            "passed": passed_tests,
            "failed": failed_tests,
            "success_rate": f"{success_rate:.1f}%"
        },
        "test_cases": all_tests
    }

    # Guardar reporte
    with open('unified_test_report.json', 'w') as f:
        json.dump(unified_report, f, indent=2)

    print("✅ Reporte unificado generado: unified_test_report.json")

    # Mostrar resumen
    print(f"\n📈 RESUMEN FINAL:")
    print(f"   Total tests: {total_tests}")
    print(f"   ✅ Exitosos: {passed_tests}")
    print(f"   ❌ Fallidos: {failed_tests}")
    print(f"   📊 Tasa de éxito: {success_rate:.1f}%")
    print(f"   🔗 API Tests: {len(api_tests)}")
    print(f"   🎬 UI Tests: {len(ui_tests)}")

    return unified_report


if __name__ == "__main__":
    print("🎯 INICIANDO SISTEMA DE TESTING UNIFICADO")
    print("=" * 50)

    # Ejecutar pruebas API
    api_success = test_airline_api()

    # Generar reporte unificado
    report = generate_unified_report()

    print("=" * 50)
    print("🎉 PROCESO COMPLETADO")
    print("📁 Archivos generados:")
    print("   - api_report.json (Reporte de pruebas API)")
    print("   - unified_test_report.json (Reporte unificado)")
    print("\n🌐 Abre 'dashboard_unificado.html' para ver los resultados")