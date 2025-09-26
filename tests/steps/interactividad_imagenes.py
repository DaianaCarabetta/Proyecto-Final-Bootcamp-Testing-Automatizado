from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import locators


# @given('que el usuario está en la sección de alimentos')
# def step_impl(context):
#     context.driver = iniciar_navegador()
#     context.driver.get(f"{base_url}/alimentos")
#     assert "Alimentos" in context.driver.title

def obtener_imagen_palomitas(context):
    wait = WebDriverWait(context.driver, 10)
    return wait.until(EC.presence_of_element_located((By.XPATH, locators.PALOMITAS_IMAGE_XPATH)))

@when('mueve el cursor sobre la imagen de las palomitas')
def mover_cursor_sobre_palomitas(context):
    palomitas = obtener_imagen_palomitas(context)
    ActionChains(context.driver).move_to_element(palomitas).perform()

# confirmacion funcional, prevencion de regresiones y accesibilidad visual
@then('el cursor cambia de una flecha a una mano')
def verificar_cursor_mano(context):
    palomitas = obtener_imagen_palomitas(context)
    cursor_style = palomitas.value_of_css_property("cursor")
    print(f"Estilo de cursor detectado: {cursor_style}")
    assert cursor_style == "pointer", f"Se esperaba 'pointer', pero se obtuvo '{cursor_style}'"