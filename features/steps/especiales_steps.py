from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#steps definitions
@given('El usuario debe estar en el sitio https://fake-cinema.vercel.app/')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://fake-cinema.vercel.app/")
    print("paso 1")

@when('El usuario ingresa a la opción películas')
def step_impl(context):
    peliculas_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Películas"))
    )
    peliculas_button.click()
    print("paso 2")


@then('Debe decir el título "Los mismos héroes, como antes" en plural')
def step_impl(context):
    titulo = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert titulo.text == "Los mismos héroes, como antes"
    context.driver.quit()
    print("paso 3")

