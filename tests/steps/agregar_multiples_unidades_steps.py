import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils.locators import SHOW_CART_LINK_XPATH
from utils.locators import PALOMITAS_IMAGE_XPATH, ADD_TO_CART_BUTTON_XPATH
from steps.config_browser import iniciar_navegador, base_url


@given('que el usuario está en la sección de alimentos')
def step_ir_a_seccion_alimentos(context):
    navegador = context.config.userdata.get("navegador", "chrome")
    print(f"🧭 Navegador seleccionado: {navegador}")
    context.driver = iniciar_navegador(navegador)
    context.base_url = base_url
    context.driver.get(f"{context.base_url}/alimentos")
    context.wait = WebDriverWait(context.driver, 10)

@when('hago clic 3 veces en el botón "Agregar" para las "Palomitas"')
def step_agregar_palomitas(context):
    print("🍿 Haciendo clic en palomitas")
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, PALOMITAS_IMAGE_XPATH))
    ).click()

    boton_agregar = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ADD_TO_CART_BUTTON_XPATH))
    )

    for _ in range(3):
        boton_agregar.click()
        time.sleep(0.5)

@then('la cantidad de "Palomitas" en el carrito es 3')
def step_verificar_palomitas_en_carrito(context):
    print("🛒 Verificando cantidad en el carrito")
    # Abrir el carrito
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, SHOW_CART_LINK_XPATH))
    ).click()

    # Verificar el contenido del carrito
    xpath_cantidad = f'//span[contains(normalize-space(.), "Palomitas x 3")]'

    try:
        elemento = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_cantidad))
        )
        assert "Palomitas x 3" in elemento.text

        time.sleep(2)

    finally:
        time.sleep(5)  # Espera antes de cerrar
        context.driver.quit()