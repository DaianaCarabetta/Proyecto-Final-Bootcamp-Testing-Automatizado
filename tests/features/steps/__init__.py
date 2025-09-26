import sys
import os

# Agrega la carpeta 'tests' al path
tests_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if tests_path not in sys.path:
    sys.path.insert(0, tests_path)

# Importa todos los steps desde tests.steps
from steps.agregar_multiples_unidades_steps import *

print("✅ Steps redirigidos correctamente desde tests/steps")
