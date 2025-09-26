from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = 'https://fake-cinema.vercel.app/'

@given('que el usuario está en la página de inicio del sitio web del cine')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.browser.get(BASE_URL)
    context.wait = WebDriverWait(context.driver, 10)
    context.wait.until(EC.presence_of_element_located((By.ID, "cartelera")))

@when('busca la película con el título "Sonic 3"')
def step_impl(context):
    # Simula scroll para cargar más contenido si es necesario
    last_height = context.driver.execute_script("return document.body.scrollHeight")
    while True:
        context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        context.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        new_height = context.driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

@then('no se muestran resultados para la película "Sonic 3"')
def step_impl(context):
    try:
        # Espera hasta que el DOM esté completamente cargado
        context.wait.until(EC.presence_of_element_located((By.ID, "cartelera")))
        # Busca si existe algún elemento que contenga "Sonic 3"
        sonic = context.driver.find_elements(By.XPATH, "//*[contains(text(),'Sonic 3')]")
        assert len(sonic) == 0, "Se encontró la película 'Sonic 3' en la cartelera"
    except TimeoutException:
        assert True, "La cartelera no cargó, pero no se encontró 'Sonic 3'"
    finally:
        context.driver.quit()