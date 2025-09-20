from behave import then, when
from page_objects.checkout_page import CheckoutPage


@then("debería visualizar la lista de productos seleccionados con su precio unitario")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    assert checkout_page.is_item_displayed("Palomitas", "$3.50")
    assert checkout_page.is_item_displayed("Hot Dog", "$4.00")

@then("debería visualizar el total de la compra")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    assert checkout_page.get_total() is not None


@when("intenta confirmar con un email inválido")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.fill_field("email", "correo-invalido")
    checkout_page.confirm_payment()

@then("el sistema debe mostrar un mensaje de error")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    validation_message = checkout_page.get_field_validation_message("email")

    assert validation_message != "", "No se mostró mensaje de validación en el campo email"
    expected_keywords = ["include an '@'", "missing an '@'", "correo", "email"]
    assert any(keyword in validation_message.lower() for keyword in expected_keywords), \
        f"El mensaje no corresponde a email inválido: {validation_message}"


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

    assert validation_message != "", "No se mostró mensaje de validación en el campo Apellido"
    normalized = validation_message.lower().strip()

    expected_keywords = [
        "please fill out",
        "rellene este campo",
        "completa este campo"
    ]
    assert any(keyword in normalized for keyword in expected_keywords), \
        f"El mensaje no corresponde a un campo obligatorio: {validation_message}"


@when("el usuario completó el formulario de checkout con datos válidos y confirmó el pago")
def step_impl(context):
    checkout_page = CheckoutPage(context.driver)
    checkout_page.fill_form(
        nombre="Daiana",
        apellido="Carabetta",
        email="dai.carabetta@example.com",
        card_name="Daiana Carabetta",
        card_number="4111111111111111",
        cvv="123",
    )

    context.page = checkout_page.confirm_payment()


@then("el sistema debería redirigirlo a la vista de confirmación de pago")
def step_impl(context):
    assert context.page.is_loaded(), "La página de confirmación no se cargó correctamente."
