from behave import given, when, then
from selenium import webdriver

@given('que estoy en la pantalla de selección de Promos')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://tusitio.com/promos")  # Ajusta la URL

@when('el combo "Pareja" está disponible')
def step_impl(context):
    combo = context.driver.find_element("xpath", "//div[contains(text(), 'Combo Pareja')]")
    assert combo.is_displayed(), "El combo 'Pareja' no está disponible"

@when('selecciono el combo "Pareja"')
def step_impl(context):
    combo = context.driver.find_element("xpath", "//div[contains(text(), 'Combo Pareja')]")
    combo.click()

@when('el sistema debe redirigirme a la pantalla de selección de sillas')
def step_impl(context):
    assert "sillas" in context.driver.current_url, "No se redirigió a la pantalla de selección de sillas"

@then('después de seleccionar las sillas, debe redirigirme a la pantalla de pago')
def step_impl(context):
    # Simula selección de sillas
    silla = context.driver.find_element("class name", "silla-disponible")
    silla.click()
    continuar = context.driver.find_element("id", "continuar")
    continuar.click()
    assert "pago" in context.driver.current_url, "No se redirigió a la pantalla de pago"
    context.driver.quit()
