import json
import subprocess
from datetime import datetime


def generate_json_report():
    # Ejecutar pytest y obtener resultados en JSON
    result = subprocess.run([
        'pytest', 'api_tests/', '-v', '--json-report',
        '--json-report-file=test_report.json'
    ], capture_output=True, text=True)

    # Leer y mejorar el reporte JSON
    with open('test_report.json', 'r') as f:
        report = json.load(f)

    # Agregar metadata adicional
    enhanced_report = {
        "project": "Airline API Automation",
        "environment": "Testing",
        "api_url": "https://cf-automation-airline-api.onrender.com",
        "execution_date": datetime.now().isoformat(),
        "summary": {
            "total_tests": report['summary']['total'],
            "passed": report['summary']['passed'],
            "failed": report['summary']['failed'],
            "skipped": report['summary']['skipped'],
            "success_rate": f"{(report['summary']['passed'] / report['summary']['total'] * 100):.1f}%"
        },
        "test_cases": []
    }

    # Agregar detalles de cada test
    for test in report['tests']:
        enhanced_report['test_cases'].append({
            "name": test['nodeid'],
            "outcome": test['outcome'],
            "duration": test['duration'],
            "module": test['nodeid'].split('::')[0]
        })

    # Guardar reporte mejorado
    with open('enhanced_test_report.json', 'w') as f:
        json.dump(enhanced_report, f, indent=2)

    print("✅ Reporte JSON generado: enhanced_test_report.json")


if __name__ == "__main__":
    generate_json_report()