from behave import when, then
from selenium.common.exceptions import TimeoutException

@when('agrega {cantidad:d} unidades de "{producto}" al carrito')
def step_agregar_muchas_unidades(context, cantidad, producto):
    context.alimentos_page.ir_a_producto(producto)
    context.alimentos_page.agregar_producto(cantidad)


@then('se muestra un mensaje de error indicando que se alcanzó el límite máximo permitido')
def step_verificar_mensaje_error(context):
    """
    Verifica que se muestre un mensaje de error cuando se intenta
    agregar más de la cantidad máxima permitida de un producto.
    """
    try:
        mensaje_error = context.alimentos_page.obtener_mensaje_error_limite()
        if mensaje_error:
            print(f"✅ Mensaje de error detectado: {mensaje_error}")
        else:
            print("⚠️ BUG: Debería tener un límite de productos y se debería mostrar un mensaje de error.")
        assert mensaje_error is not None, "❌ No se mostró mensaje de error por límite de unidades."
    except TimeoutException:
        print("⚠️ BUG: Debería tener un límite de productos y se debería mostrar un mensaje de error.")
        assert False, "❌ No se detectó mensaje de error dentro del tiempo esperado."
    finally:
        context.driver.quit()
