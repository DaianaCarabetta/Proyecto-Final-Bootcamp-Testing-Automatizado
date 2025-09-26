from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://fake-cinema.vercel.app/'

@given('que estoy en la interfaz de programación de películas')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(BASE_URL)
    context.wait = WebDriverWait(context.driver, 10)
    context.wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Cartelera']")))

@when('hay una película con clasificación visible (por ejemplo, "B")')
def step_impl(context):
    context.clasificacion = context.driver.find_element(By.XPATH, "//div[normalize-space()='B']")
    assert context.clasificacion.is_displayed(), "La clasificación 'B' está visible"

@when('paso el cursor sobre la clasificación de la película')
def step_impl(context):
    ActionChains(context.driver).move_to_element(context.clasificacion).perform()

@then('el botón relacionado no debe cambiar a color negro')
def step_impl(context):
    boton = context.driver.find_element(By.XPATH, "//div[normalize-space()='B']")
    color = boton.value_of_css_property("rgb(234 179 8 / var(--tw-bg-opacity, 1))")
    assert color != "rgb(0, 0, 0)", f"El botón cambió a color negro: {color}"
    context.driver.quit()
