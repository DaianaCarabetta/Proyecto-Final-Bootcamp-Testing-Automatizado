from behave import given, when, then
from page_objects.home_page import HomePage


@given("que el usuario está en la página de inicio")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.open()


@when("el carrusel de películas se ha cargado correctamente")
def step_impl(context):
    assert context.home_page.is_carousel_loaded(), "El carrusel no se cargó correctamente"


@when("presiona el botón de la flecha derecha del carrusel")
def step_impl(context):
    context.home_page.click_carousel_next()


@then("el carrusel muestra una película disponible")
def step_impl(context):
    assert context.home_page.is_any_movie_visible_in_carousel(), "El carrusel no mostró ninguna película disponible"


@when("el usuario navega a la sección de cartelera")
def step_impl(context):
    context.home_page.scroll_to_cartelera()
    assert context.home_page.is_cartelera_loaded(), "La cartelera no se cargó"


@then("debería ver los títulos de las películas disponibles")
def step_impl(context):
    assert context.home_page.has_movies_listed(), "No se muestran películas en la cartelera"


@when("selecciona la película {movie}")
def step_impl(context, movie):
    movie = movie.strip('"').strip("'")
    context.home_page.select_movie(movie)


@then("el sistema lo redirige al detalle de la película {movie}")
def step_impl(context, movie):
    movie = movie.strip('"').strip("'")
    assert context.home_page.is_movie_detail_loaded(movie), f"No se cargó el detalle de {movie}"
    current = context.home_page.get_current_url()
    expected = context.home_page.expected_movie_detail_url(movie)
    assert expected in current, f"Esperaba URL que contenga '{expected}', pero está '{current}'"
