from behave import given, when, then
from selenium import webdriver
from page_objects.alimentos_page import AlimentosPage

@given('que el usuario está en la sección de alimentos')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.alimentos_page = AlimentosPage(context.driver)
    context.alimentos_page.ir_a_seccion_alimentos()

@when('hago clic {cantidad:d} veces en el botón "Agregar" para las "{producto}"')
def step_impl(context, cantidad, producto):
    context.alimentos_page.ir_a_producto(producto)
    context.alimentos_page.agregar_producto(cantidad)

@then('la cantidad de "{producto}" en el carrito es {cantidad:d}')
def step_impl(context, producto, cantidad):
    cantidad_obtenida = context.alimentos_page.obtener_cantidad_producto(producto, cantidad)
    assert cantidad_obtenida == cantidad, f"Se esperaba {cantidad} pero se obtuvo {cantidad_obtenida}"
    context.driver.quit()


