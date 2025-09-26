from behave import given, when, then
from page_objects.cart_page import CartPage

URL_ALIMENTOS = "https://fake-cinema.vercel.app/alimentos"
URL_CHECKOUT = "https://fake-cinema.vercel.app/checkout"


@given('el usuario accede a la vista de Alimentos')
def step_impl(context):
    context.driver.get(URL_ALIMENTOS)
    context.cart_page = CartPage(context.driver)


@when('selecciona "{item}"')
def step_impl(context, item):
    context.cart_page.select_item(item)


@when('hace clic en "Agregar al carrito"')
def step_impl(context):
    context.cart_page.add_to_cart()


@when('vuelve a la vista de Alimentos')
def step_impl(context):
    context.cart_page.go_back_to_alimentos()


@when('accede a la vista de Carrito')
def step_impl(context):
    context.cart_page.go_to_cart()

@then("debería visualizar la vista de Carrito cargada correctamente")
def step_impl(context):
    assert context.cart_page.is_cart_loaded(), "La vista de Carrito no se cargó correctamente"


@then('debería ver "{item}" con su precio "{price}"')
def step_impl(context, item, price):
    assert context.cart_page.is_item_displayed(item, price)


@then('debería visualizar el subtotal "{subtotal}"')
def step_impl(context, subtotal):
    assert context.cart_page.get_subtotal() == subtotal


@then('debería visualizar el total "{total}"')
def step_impl(context, total):
    assert context.cart_page.get_total() == total


@when('hace clic en "Proceder al pago"')
def step_impl(context):
    context.cart_page.click_checkout()


@then('el sistema debería redirigirlo a la vista de checkout')
def step_impl(context):
    assert URL_CHECKOUT in context.driver.current_url
