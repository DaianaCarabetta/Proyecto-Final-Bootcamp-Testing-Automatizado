from behave import given, when, then
from page_objects.promos_page import PromosPage

@given("que estoy en la pantalla de Promos")
def step_open_promos(context):
    context.promos_page = PromosPage(context.driver)
    context.promos_page.open()

@when("el Combo Pareja está disponible")
def step_check_combo_pareja(context):
    assert context.promos_page.is_combo_pareja_available(), "El Combo Pareja no está disponible"

@when("selecciono el Combo Pareja")
def step_select_combo_pareja(context):
    context.promos_page.select_combo_pareja()
    assert context.promos_page.is_combo_pareja_page_loaded(), "No se abrió la página del Combo Pareja"

@when("agrego el Combo Pareja al carrito")
def step_agregar_combo_pareja(context):
    context.promos_page.click_agregar_al_carrito()

@then("el sistema debe redirigirme a la pantalla de selección de asientos")
def step_verify_seat_selection(context):
    assert context.promos_page.is_seat_selection_page_loaded(), "No se redirigió a la selección de asientos"

@then("debe redirigirme a la pantalla de pago")
def step_verify_payment_page(context):
    assert context.promos_page.is_payment_page_loaded(), "No se redirigió a la pantalla de pago"
