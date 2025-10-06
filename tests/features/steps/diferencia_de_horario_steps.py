from behave import then
from page_objects.book_page import BookPage
from selenium.webdriver.support.ui import WebDriverWait

@then("el resumen de carrito debe reflejar la fecha y el horario seleccionado")
def step_verificar_carrito(context):
    """
    Compara la selección del usuario (guardada en context) contra lo que muestra el carrito.
    Debido al bug, siempre devuelve "Hoy, 27 de julio, 10:00 pm", lo que provocará fallo.
    """
    context.book_page = BookPage(context.driver)
    carrito_texto = context.book_page.obtener_horario_carrito()
    expected_text = f"Hoy, {context.fecha_seleccionada}, {context.horario_seleccionado}"

    assert carrito_texto == expected_text, (
        f"❌ Carrito muestra '{carrito_texto}' pero debería mostrar '{expected_text}'"
    )


@then("no deben aparecer en Fecha y hora Hoy, 27 de julio, 10:00 pm")
def step_verificar_horarios_prohibidos(context):
    """
    Verifica que la fecha y los horarios prohibidos no estén presentes en el resumen del carrito.
    """
    context.book_page = BookPage(context.driver)
    assert context.book_page.validar_no_horarios_prohibidos(), \
        "❌ Se encontraron fecha y horario que no coinciden con el seleccionado en el resumen de carrito."
    print("✅ No se encontraron fecha y horarios prohibidos en el carrito.")
