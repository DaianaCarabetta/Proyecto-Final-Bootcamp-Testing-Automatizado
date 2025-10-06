from behave import given, when, then
from page_objects.checkout_page import CheckoutPage


@given("el usuario está en la vista de checkout")
def step_impl(context):
    context.page = CheckoutPage(context.driver)
    assert context.page.is_loaded(), "La página de checkout no se cargó correctamente."


@when('ingresa números en el campo "Nombre en la tarjeta"')
def step_impl(context):
    context.page.fill_field("cardName", "123456")
    context.page.confirm_payment()


@then("el sistema debería mostrar un error indicando que solo se permiten letras")
def step_impl(context):
    mensaje = context.page.get_field_validation_message("cardName")
    if mensaje == "":
        print("BUG: No se mostró error en el campo Nombre en la tarjeta.")
    assert mensaje != "", "No se mostró error en el campo Nombre en la tarjeta."



@when('ingresa texto en el campo "Número de tarjeta"')
def step_impl(context):
    context.page.fill_field("cardNumber", "abcd efgh ijkl")
    context.page.blur_field("cardNumber")


@then("el sistema debería mostrar un error indicando que solo se permiten números")
def step_impl(context):
    mensaje = context.page.get_field_validation_message("cardNumber")
    if mensaje == "":
        print("BUG: No se mostró error en el campo Número de tarjeta.")
    assert mensaje != "", "No se mostró error en el campo Número de tarjeta."


@when('ingresa texto en el campo "CVV"')
def step_impl(context):
    context.page.fill_field("cvv", "abc")
    context.page.blur_field("cvv")


@then("el sistema debería mostrar un error indicando que solo se permiten números de 3 o 4 dígitos")
def step_impl(context):
    mensaje = context.page.get_field_validation_message("cvv")
    if mensaje == "":
        print("BUG: No se mostró error en el campo CVV.")
    assert mensaje != "", "No se mostró error en el campo CVV."


@then("el botón de confirmación de pago debería estar deshabilitado")
def step_impl(context):
    enabled = context.page.is_confirm_button_enabled()
    if enabled:
        print("BUG: El botón de confirmación de pago está habilitado cuando debería estar deshabilitado.")
    assert not enabled, "El botón de confirmación de pago no está deshabilitado cuando debería."
