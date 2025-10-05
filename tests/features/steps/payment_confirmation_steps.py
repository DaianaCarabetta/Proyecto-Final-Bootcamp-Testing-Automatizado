from behave import given, when, then
from page_objects.payment_confirmation_page import ConfirmationPage
import re


@given("el usuario está en la vista de confirmación de pago")
def step_impl(context):
    context.page = ConfirmationPage(context.driver)
    assert context.page.is_loaded(), "La página de confirmación no se cargó correctamente."


@then("se muestra la vista de confirmación de pago")
def step_impl(context):
    context.page = ConfirmationPage(context.driver)
    assert context.page.is_loaded(), "La vista de confirmación no está disponible."


@then("debería visualizar un resumen de la compra con los productos adquiridos y el detalle")
def step_impl(context):
    assert context.page.is_purchase_summary_displayed(), "El resumen de compra no se visualiza."


@then("debería visualizar el monto total de la compra")
def step_impl(context):
    total = context.page.get_total_amount()
    assert total != "", "El monto total de la compra no se visualiza."


@then("debería visualizar un número de compra único")
def step_impl(context):
    order_number = context.page.get_order_number()
    assert re.search(r"\d+", order_number), f"Número de compra inválido: {order_number}"


@when('hace clic en el botón "Volver al inicio"')
def step_impl(context):
    context.page.click_return_home()


@then("el sistema debería redirigirlo a la página de inicio")
def step_impl(context):
    assert "home" in context.driver.current_url or context.driver.current_url.endswith("/"), \
        f"Redirección inesperada: {context.driver.current_url}"
