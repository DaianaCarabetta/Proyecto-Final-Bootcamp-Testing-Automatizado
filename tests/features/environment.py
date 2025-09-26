import sys
import os

# Agrega la raíz del proyecto al path para que Python reconozca 'utils'
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Agrega la carpeta 'tests' al path
tests_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if tests_path not in sys.path:
    sys.path.insert(0, tests_path)

# Ahora sí puedes importar los hooks
from utils.environment import before_all, before_scenario, after_scenario
