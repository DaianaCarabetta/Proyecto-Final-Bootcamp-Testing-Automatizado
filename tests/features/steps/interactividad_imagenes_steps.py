from behave import when, then
from page_objects.alimentos_page import AlimentosPage

@when('mueve el cursor sobre la imagen de unas {producto}')
def step_impl(context, producto):
    if not hasattr(context, 'alimentos_page'):
        context.alimentos_page = AlimentosPage(context.driver)
    context.alimentos_page.hover_producto(producto)
    print(f"Hover realizado sobre {producto}")

@then('el cursor cambia de una flecha a una mano')
def step_impl(context):
    cursor = context.alimentos_page.obtener_cursor_hover()
    print("Cursor actual:", cursor)
    assert cursor in ["pointer", "hand", "grab"], f"Cursor esperado 'pointer/hand/grab', pero se obtuvo '{cursor}'"
