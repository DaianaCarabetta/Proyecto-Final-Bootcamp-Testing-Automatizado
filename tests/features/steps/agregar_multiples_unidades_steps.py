from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://fake-cinema.vercel.app/'

@given('que el usuario está en la sección de alimentos')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(BASE_URL)
    wait = WebDriverWait(context.driver, 10)
    alimentos_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Alimentos')))
    alimentos_button.click()

@when('hago clic 3 veces en el botón "Agregar" para las "Palomitas de Maíz"')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    agregar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Agregar al carrito']")))
    for _ in range(3):
        agregar_button.click()

@then('la cantidad de "Palomitas de Maíz" en el carrito es 3')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    carrito_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']")))
    carrito_button.click()
    cantidad_palomitas = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Palomitas x 3']")))
    assert cantidad_palomitas.text == '3', f"Se esperaba 3 pero se obtuvo {cantidad_palomitas.text}"
    context.driver.quit()

