from behave import given, when, then
from selenium import webdriver

@given('que el usuario se encuentra en la página de inicio')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://tusitio.com")  # Reemplaza con tu URL

@when('hace scroll en la cartelera')
def step_impl(context):
    cartelera = context.driver.find_element("id", "cartelera")  # Ajusta el selector
    context.driver.execute_script("arguments[0].scrollIntoView();", cartelera)

@when('hace clic en la palabra "Horarios"')
def step_impl(context):
    horarios = context.driver.find_element("link text", "Horarios")
    horarios.click()

@then('no ocurre ninguna acción ni redirección')
def step_impl(context):
    current_url = context.driver.current_url
    assert current_url == "https://tusitio.com", "La URL cambió, hubo una redirección"
    # También podrías verificar que no se abrió un modal, no hubo cambios en el DOM, etc.
    context.driver.quit()
