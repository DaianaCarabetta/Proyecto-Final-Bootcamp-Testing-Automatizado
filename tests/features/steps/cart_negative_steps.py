from behave import given, when, then
from page_objects.cart_page import CartPage


@given("el usuario tiene productos en el carrito")
def step_impl(context):
    context.cart_page = CartPage(context.driver)
    assert context.cart_page.has_items(), "El carrito debería tener productos cargados"


@when("intenta eliminar un producto del carrito")
def step_impl(context):
    # No se hace clic porque la app no tiene botón de eliminar
    pass


@then("debería existir un botón o acción para eliminarlo")
def step_impl(context):
    exists = context.cart_page.has_remove_button()
    if not exists:
        print("BUG: No se encontró un botón de eliminar, pero debería existir.")
    assert exists, "No se encontró un botón de eliminar, pero debería existir"


@when("quiere aumentar la cantidad de un producto")
def step_impl(context):
    # No se hace clic porque la app no tiene botón de aumentar
    pass


@then("debería existir un botón o control para incrementarla")
def step_impl(context):
    exists = context.cart_page.has_increase_button()
    if not exists:
        print("BUG: No se encontró un control de incremento, pero debería existir.")
    assert exists, "No se encontró un control de incremento, pero debería existir"


@when("quiere disminuir la cantidad de un producto")
def step_impl(context):
    # No se hace clic porque la app no tiene botón de disminuir
    pass


@then("debería existir un botón o control para reducirla")
def step_impl(context):
    exists = context.cart_page.has_decrease_button()
    if not exists:
        print("BUG: No se encontró un control de decremento, pero debería existir.")
    assert exists, "No se encontró un control de decremento, pero debería existir"