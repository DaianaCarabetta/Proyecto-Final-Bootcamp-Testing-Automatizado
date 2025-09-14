from behave import then, when
from page_objects.checkout_page import CheckoutPage

# ---------- Visualizar resumen ----------
@then("debería visualizar la lista de productos seleccionados con su precio unitario")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    assert checkout_page.is_item_displayed("Palomitas", "$3.50")
    assert checkout_page.is_item_displayed("Hot Dog", "$4.00")


@then("debería visualizar el total de la compra")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    assert checkout_page.get_total() is not None


# ---------- Validación de email ----------
@when("ingresa un email con formato inválido")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.fill_field("email", "correo-invalido")
    checkout_page.confirm_payment()


@then("el sistema debe mostrar un mensaje de error y el boton debe estar deshabilitado")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    validation_message = checkout_page.get_field_validation_message("email")

    # Asegurarse que exista algún mensaje de error
    assert validation_message != ""

    # Botón no debe estar habilitado
    assert not checkout_page.is_confirm_button_enabled()


# ---------- Validación de campos obligatorios ----------
@when('deja vacío el campo "Apellido"')
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.fill_field("lastName", "")
    checkout_page.blur_field("lastName")


@when("confirma la compra")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.confirm_payment()


@then("el sistema debe mostrar un mensaje de error indicando que el campo es obligatorio")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    validation_message = checkout_page.get_field_validation_message("lastName")

    # Asegurarse que haya mensaje de error
    assert validation_message != ""

    # Aceptar idioma español o inglés
    assert (
        "Please fill out this field" in validation_message
        or "Rellene este campo" in validation_message
    )


# ---------- Step compartido ----------
@then("no debe permitir continuar con el pago")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    assert not checkout_page.is_confirm_button_enabled()
