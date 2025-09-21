from behave import given, when, then
from selenium import webdriver

@given('que una película está programada con las opciones de idioma "Español" y "Subtitulada"')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://tusitio.com/programacion")  # Ajusta la URL
    context.pelicula = context.driver.find_element("class name", "pelicula-programada")

@when('estas opciones son visibles en la interfaz de programación')
def step_impl(context):
    idioma_es = context.pelicula.find_element("xpath", ".//span[contains(text(), 'Español')]")
    idioma_sub = context.pelicula.find_element("xpath", ".//span[contains(text(), 'Subtitulada')]")
    assert idioma_es.is_displayed() and idioma_sub.is_displayed(), "Las opciones de idioma no están visibles"

@when('presiono el botón "Refrescar"')
def step_impl(context):
    refrescar = context.driver.find_element("id", "btn-refrescar")
    refrescar.click()

@when('las opciones de idioma "Español" y "Subtitulada" deben permanecer visibles')
@then('no deben desaparecer ni cambiar aleatoriamente')
def step_impl(context):
    idioma_es = context.pelicula.find_element("xpath", ".//span[contains(text(), 'Español')]")
    idioma_sub = context.pelicula.find_element("xpath", ".//span[contains(text(), 'Subtitulada')]")
    assert idioma_es.is_displayed() and idioma_sub.is_displayed(), "Las opciones de idioma desaparecieron o cambiaron"
    context.driver.quit()
