import json
import subprocess
from datetime import datetime
import os


def generate_unified_report():
    # Ejecutar pruebas y generar reporte JSON
    result = subprocess.run([
        'pytest', 'tests/', '-v', '--json-report',
        '--json-report-file=test_report.json'
    ], capture_output=True, text=True)

    # Leer reporte base
    with open('test_report.json', 'r') as f:
        report = json.load(f)

    # Clasificar tests en API y UI
    test_cases = []
    for test in report['tests']:
        test_type = 'UI' if 'ui' in test['nodeid'].lower() or 'browser' in test['nodeid'].lower() else 'API'
        module = test['nodeid'].split('::')[0].replace('_', ' ').title()

        test_cases.append({
            "type": test_type,
            "module": module,
            "name": test['nodeid'].split('::')[-1],
            "status": test['outcome'],
            "duration": f"{test['duration']:.0f}ms",
            "error": test.get('call', {}).get('crash', {}).get('message', '') if test['outcome'] == 'failed' else None
        })

    # Crear reporte unificado mejorado
    enhanced_report = {
        "project": "Airline App - UI & API Testing",
        "environment": "Testing",
        "api_url": "https://cf-automation-airline-api.onrender.com",
        "ui_url": "https://your-ui-app.com",
        "execution_date": datetime.now().isoformat(),
        "summary": {
            "total_tests": report['summary']['total'],
            "passed": report['summary']['passed'],
            "failed": report['summary']['failed'],
            "skipped": report['summary']['skipped'],
            "success_rate": f"{(report['summary']['passed'] / report['summary']['total'] * 100):.1f}%"
        },
        "test_cases": test_cases
    }

    # Guardar reporte mejorado
    with open('unified_test_report.json', 'w') as f:
        json.dump(enhanced_report, f, indent=2)

    print("✅ Reporte unificado generado: unified_test_report.json")
    return enhanced_report


def generate_html_dashboard():
    # Generar dashboard HTML con los datos del reporte
    with open('unified_test_report.json', 'r') as f:
        report_data = json.load(f)

    # Aquí podrías generar el HTML dinámicamente o usar una plantilla
    print("📊 Dashboard HTML listo para ser generado con los datos actualizados")

    return report_data


if __name__ == "__main__":
    # Generar reporte unificado
    report = generate_unified_report()

    # Mostrar resumen en consola
    print(f"\n📈 RESUMEN DE EJECUCIÓN:")
    print(f"   Total tests: {report['summary']['total_tests']}")
    print(f"   Exitosos: {report['summary']['passed']}")
    print(f"   Fallidos: {report['summary']['failed']}")
    print(f"   Tasa de éxito: {report['summary']['success_rate']}")

    # Contar tests por tipo
    api_tests = len([t for t in report['test_cases'] if t['type'] == 'API'])
    ui_tests = len([t for t in report['test_cases'] if t['type'] == 'UI'])
    print(f"   Tests API: {api_tests}")
    print(f"   Tests UI: {ui_tests}")