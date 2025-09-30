from behave import when, then
from page_objects.detail_page import DetailPage


@then("debería ver el detalle de la película {movie}")
def step_impl(context, movie):
    context.detail_page = DetailPage(context.driver)
    assert context.detail_page.is_loaded(), "El detalle de la película no se cargó"

    actual_title = context.detail_page.get_title()
    assert movie.lower() in actual_title.lower(), (
        f'el detalle de la película "{movie}" no coincide, '
        f'se encontró "{actual_title}"'
    )
    context.movie_name = actual_title


@when("selecciona el día siguiente")
def step_impl(context):
    context.detail_page.select_second_day()


@when("selecciona un horario en Español")
def step_impl(context):
    showtimes = context.detail_page.get_showtimes("Español")
    assert len(showtimes) > 0, "No hay horarios en Español disponibles"
    context.detail_page.select_showtime("Español", showtimes[0])


@then("el sistema lo redirige a la página de selección de asientos")
def step_impl(context):
    assert context.detail_page.is_book_page_loaded(context.movie_name), \
        "No se redirigió a la página de selección de asientos"
