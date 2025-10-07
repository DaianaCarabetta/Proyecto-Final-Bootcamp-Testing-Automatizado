from behave import when, then
from page_objects.home_page import HomePage

@when('hace clic en la palabra "Horarios"')
def step_click_horarios(context):
    """
    Hace clic en el enlace o botón 'Horarios' en la página de inicio.
    """
    if not hasattr(context, "home_page"):
        context.home_page = HomePage(context.driver)

    context.home_page.click_horarios_link()


@then("deberia mostrar la seccion de horarios")
def step_validate_horarios_section(context):
    """
    Valida que la sección de 'Horarios' se muestre correctamente.
    """
    assert context.home_page.is_horarios_section_visible(), \
        "❌ La sección de 'Horarios' no se mostró correctamente tras hacer clic."
