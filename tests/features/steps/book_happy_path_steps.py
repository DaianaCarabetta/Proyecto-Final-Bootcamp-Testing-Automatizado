from behave import when, then
from page_objects.book_page import BookPage


@when('el usuario selecciona el asiento "{seat}"')
def step_impl(context, seat):
    row, number = seat[0], seat[1:]
    context.book_page = BookPage(context.driver)
    assert context.book_page.is_loaded(), "La página de selección de asientos no cargó correctamente"
    context.book_page.select_seat(row, number)


@when('hace clic en "Comprar boletos"')
def step_impl(context):
    context.book_page.click_buy()


@when('en el modal ingresa "{adults}" en Adultos')
def step_impl(context, adults):
    context.book_page.fill_modal_tickets(adults=int(adults))


@when("confirma la selección")
def step_impl(context):
    pass


@then("el sistema lo redirige al carrito")
def step_impl(context):
    assert context.book_page.is_cart_page_loaded(), "No se redirigió al carrito"
