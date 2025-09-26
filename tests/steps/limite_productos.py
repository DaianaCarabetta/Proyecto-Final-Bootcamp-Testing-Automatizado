from datetime import datetime
import os
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import locators
import time

@when('agrega 101 unidades de "Palomitas de Maíz" al carrito')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    palomitas = wait.until(EC.element_to_be_clickable((By.XPATH, locators.PALOMITAS_IMAGE_XPATH)))
    palomitas.click()

    boton_agregar = wait.until(EC.element_to_be_clickable((By.XPATH, locators.ADD_TO_CART_BUTTON_XPATH)))

    for i in range(101):
        boton_agregar.click()
        time.sleep(0.05)
        print(f"Unidad {i + 1} agregada")

@when('la cantidad de "Palomitas de Maíz" en el carrito es de 101')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    boton_carrito = wait.until(EC.element_to_be_clickable((By.XPATH, locators.SHOW_CART_LINK_XPATH)))
    boton_carrito.click()

    xpath_cantidad = '//span[contains(normalize-space(.), "Palomitas x 101")]'
    cantidad_elemento = wait.until(EC.presence_of_element_located((By.XPATH, xpath_cantidad)))

    assert cantidad_elemento is not None, (
        "❌ Resultado inesperado: No se encontró el texto 'Palomitas x 101' en el carrito. "
        "✅ Resultado esperado: El carrito debería mostrar 'Palomitas x 101' si se agregaron correctamente."
    )

@then('no se muestra ningún mensaje de error')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)

    boton_carrito = wait.until(EC.element_to_be_clickable((By.XPATH, locators.SHOW_CART_LINK_XPATH)))
    boton_carrito.click()

    # 📸 Captura de pantalla del carrito final
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"carrito_final_{timestamp}.png"
    ruta_evidencia = os.path.join("Proyecto-Final-Bootcamp-Testing-Automatizado", "Evidencia", filename)
    context.driver.save_screenshot(ruta_evidencia)
    print(f"📸 Screenshot del carrito guardada en: {ruta_evidencia}")

    errores = context.driver.find_elements(By.XPATH, '//div[contains(@class, "error") or contains(text(), "límite")]')
    assert len(errores) > 0, (
        "❌ Test fallido: El sistema permitió agregar más de 100 unidades sin mostrar un mensaje de error. "
        "✅ Se esperaba una restricción que impidiera esta acción por motivos de negocio."
    )