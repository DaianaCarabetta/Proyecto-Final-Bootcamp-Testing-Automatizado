from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

# ---
# Feature: Visualizar títulos de películas
# ---

@given('El usuario debe estar en el sitio {url}')
def step_given_user_is_on_site(context, url):
    """Given El usuario debe estar en el sitio https://fake-cinema.vercel.app/"""
    context.driver.get(url)

@when('El usuario ingresa a la opción peliculas')
def step_when_user_goes_to_movies(context):
    """When El usuario ingresa a la opción peliculas"""
    # Lógica para encontrar y hacer clic en el enlace/botón "Películas"
    pass

@then('Debe decir el título "{title}" en plural')
def step_then_should_see_title(context, title):
    """Then Debe decir el título "Los mismos héroes, como antes" en plural"""
    # Lógica para encontrar el elemento del título y verificar su texto
    assert context.driver.find_element(By.Xpath,
                                       "(//h2[contains(text(), 'héroe')])[1]").text == "Los mismos héroes, como antes"
    pass

@given('que el usuario se encuentra en la página de inicio')
def step_given_user_is_on_home_page(context):
    """Given que el usuario se encuentra en la página de inicio"""
    # Asume que el navegador ya está en la página principal
    pass

@when('el usuario navega a la URL del sitio web {url}')
def step_when_user_navigates_to_url(context, url):
    """When el usuario navega a la URL del sitio web https://fake-cinema.vercel.app/"""
    context.driver.get(url)

@when('debería ver la página principal con la cartelera actual')
def step_and_should_see_main_page(context):
    """And debería ver la página principal con la cartelera actual"""
    # Lógica para verificar la presencia de elementos de la cartelera
    # Por ejemplo: assert context.driver.find_element(By.ID, "movie-list").is_displayed()
    pass

@then('debería poder ver los títulos de las películas disponibles')
def step_then_should_see_movie_titles(context):
    """Then debería poder ver los títulos de las películas disponibles"""
    # Lógica para verificar que los títulos de las películas son visibles
    # Por ejemplo: assert len(context.driver.find_elements(By.CLASS_NAME, "movie-title")) > 0
    pass

# ---
# Feature: Estabilidad de los horarios de funciones
# ---

@given('que la duración de la película es de {duration:d} minutos')
def step_given_movie_duration_is(context, duration):
    """Given que la duración de la película es de 140 minutos"""
    context.movie_duration = duration

@when('la sala se habilita cada {interval:d} minutos para nuevas funciones')
def step_when_room_available_interval(context, interval):
    """When la sala se habilita cada 30 minutos para nuevas funciones"""
    context.room_interval = interval

@when('existe una función programada en la Sala {room:d} a las {time}')
def step_and_existing_screening_time(context, room, time):
    """And existe una función programada en la Sala 1 a las 14:00"""
    context.existing_screening = {'room': room, 'time': time}

@when('intento programar una nueva función en la Sala {room:d} a las {new_time}')
def step_and_attempt_new_screening(context, room, new_time):
    """And intento programar una nueva función en la Sala 1 a las 14:30"""
    context.new_screening = {'room': room, 'time': new_time}
    # Lógica para interactuar con la interfaz y programar la nueva función
    # Esto puede incluir hacer clic en botones y rellenar formularios
    pass

@when('el sistema debe mostrar un mensaje de error indicando superposición de horarios')
def step_and_system_shows_error(context):
    """And el sistema debe mostrar un mensaje de error indicando superposición de horarios"""
    # Lógica para verificar que el mensaje de error aparece
    # Por ejemplo: error_message = context.driver.find_element(By.ID, "error-message")
    # context.error_message_displayed = error_message.is_displayed()
    pass

@then('no debe permitir guardar la nueva función')
def step_then_should_not_save_new_screening(context):
    """Then no debe permitir guardar la nueva función"""
    # Lógica para verificar que la función no se guardó
    # Por ejemplo: assert context.error_message_displayed
    pass

@given('que el usuario tiene una lista de funciones de películas con horarios previamente programados')
def step_given_user_has_scheduled_movies(context):
    """Given que el usuario tiene una lista de funciones de películas con horarios previamente programados"""
    # Lógica para almacenar la lista de horarios en el contexto para su posterior verificación
    # context.horarios_iniciales = get_horarios_from_page()
    pass

@when('hace clic en la película {movie_name}')
def step_when_user_clicks_on_movie(context, movie_name):
    """When hace clic en la película Superman"""
    # Lógica para encontrar y hacer clic en la película por su nombre
    pass

@when('los horarios están correctamente asignados y visibles en la interfaz')
def step_and_times_are_visible(context):
    """And los horarios están correctamente asignados y visibles en la interfaz"""
    # Lógica para verificar que los horarios se muestran
    pass

@when('presiona el botón "Refrescar"')
def step_when_presses_refresh_button(context):
    """And presiona el botón "Refrescar" """
    # Lógica para encontrar y hacer clic en el botón de refrescar
    pass

@when('los horarios de las funciones deben mantenerse sin cambios')
def step_and_times_remain_unchanged(context):
    """And los horarios de las funciones deben mantenerse sin cambios"""
    # Lógica para comparar los horarios antes y después de refrescar
    # assert context.horarios_iniciales == get_horarios_from_page()
    pass

@then('no deben generarse horarios aleatorios')
def step_then_no_random_times(context):
    """Then no deben generarse horarios aleatorios"""
    # Este paso es una reconfirmación del paso anterior, la lógica de prueba
    # ya se ha cubierto en el paso "And" anterior.
    pass

# ---
# Feature: Disponibilidad de funciones por horario
# ---

@given('que son las {time_str} AM o más tarde')
def step_given_is_1101am_or_later(context, time_str):
    """Given que son las 11:01 AM o más tarde"""
    # Lógica para simular el tiempo o comparar con la hora actual
    # context.current_time = datetime.now()
    pass

@given('que el usuario está navegando en la cartelera de películas del sitio web')
def step_given_user_is_browsing_movies(context):
    """And que el usuario está navegando en la cartelera de películas del sitio web"""
    # Lógica para ir a la página de la cartelera
    pass

@when('busca la película con la función de las {time_str} AM')
def step_when_looks_for_movie_function_at(context, time_str):
    """When busca la película con la función de las 11:00 AM"""
    # Lógica para encontrar la película y su horario
    pass

@then('la opción para comprar boletos para la función de las {time_str} AM no se muestra')
def step_then_buy_option_not_shown(context, time_str):
    """Then la opción para comprar boletos para la función de las 11:00 AM no se muestra"""
    # Lógica para verificar que el elemento no está presente o no es visible
    # Por ejemplo: try/except para buscar el elemento y afirmar que no existe
    pass

# ---
# Feature: Disponibilidad de horarios después del cierre
# ---

@given('que son las {time_str} o más tarde, hora local')
def step_given_is_2301_or_later(context, time_str):
    """Given que son las 23:01 o más tarde, hora local"""
    # Lógica para simular el tiempo después del cierre
    pass

@given('que el usuario está en la página de detalles de una película')
def step_and_user_is_on_movie_details(context):
    """And que el usuario está en la página de detalles de una película"""
    # Lógica para navegar a la página de detalles de una película
    pass

@when('revisa los horarios de las funciones para el día de hoy')
def step_when_reviews_showtimes_for_today(context):
    """When revisa los horarios de las funciones para el día de hoy"""
    # Lógica para buscar el contenedor de horarios en la página
    pass

@then('no se muestran horarios disponibles para el día actual')
def step_then_no_showtimes_are_displayed(context):
    """Then no se muestran horarios disponibles para el día actual"""
    # Lógica para verificar que no hay horarios en el contenedor
    pass

# ---
# Feature: Búsqueda de películas inexistentes
# ---

@given('que el usuario está en la página de inicio del sitio web del cine')
def step_given_user_is_on_home(context):
    """Given que el usuario está en la página de inicio del sitio web del cine"""
    # Lógica para ir a la página principal
    pass

@when('busca la película con el título "{movie_title}"')
def step_when_searches_for_movie(context, movie_title):
    """When busca la película con el título "Sonic 3" """
    # Lógica para escribir en el campo de búsqueda
    pass

@then('no se muestran resultados para la película "{movie_title}"')
def step_then_no_results_are_shown(context, movie_title):
    """Then no se muestran resultados para la película "Sonic 3" """
    # Lógica para verificar que no hay resultados
    pass

# ---
# Feature: Navegación del carrusel de películas
# ---

def step_given_user_is_at_home_page(context):
    """Given que el usuario está en la página de inicio"""
    # Asume que ya está en la página principal
    pass

@given('que el carrusel de películas se ha cargado correctamente')
def step_and_carousel_is_loaded(context):
    """And que el carrusel de películas se ha cargado correctamente"""
    # Lógica para esperar que el carrusel sea visible y esté cargado
    # wait = WebDriverWait(context.driver, 10)
    # wait.until(EC.visibility_of_element_located((By.ID, "carousel")))
    pass

@when('presiona el botón de la flecha derecha del carrusel')
def step_when_presses_right_arrow(context):
    """When presiona el botón de la flecha derecha del carrusel"""
    # Lógica para encontrar y hacer clic en el botón de la flecha derecha
    pass

@when('la siguiente película en el carrusel se vuelve visible')
def step_and_next_movie_becomes_visible(context):
    """And la siguiente película en el carrusel se vuelve visible"""
    # Lógica para verificar la visibilidad de la siguiente película
    pass

@then('el carrusel muestra la película "{movie_name}"')
def step_then_carousel_shows_movie(context, movie_name):
    """Then el carrusel muestra la película "Superman" """
    # Lógica para verificar que el título de la película es visible
    pass

# ---
# Feature: Visibilidad del carrito de alimentos
# ---

@given('que el usuario ha agregado palomitas de maíz al carrito')
def step_given_user_added_popcorn(context):
    """Given que el usuario ha agregado palomitas de maíz al carrito"""
    # Lógica para agregar palomitas al carrito
    pass

@given('que ha seleccionado un boleto de cine para una película')
def step_and_user_selected_ticket(context):
    """And que ha seleccionado un boleto de cine para una película"""
    # Lógica para seleccionar un boleto
    pass

@when('avanza a la sección de selección de asiento')
def step_when_advances_to_seat_selection(context):
    """When avanza a la sección de selección de asiento"""
    # Lógica para navegar a la sección de selección de asiento
    pass

@then('mi carrito de compras muestra las palomitas de maíz seleccionadas')
def step_then_cart_shows_popcorn(context):
    """Then mi carrito de compras muestra las palomitas de maíz seleccionadas"""
    # Lógica para verificar la visibilidad de las palomitas en el carrito
    pass

# ---
# Feature: Límite en la cantidad de productos
# ---

@given('que el usuario está en la sección de alimentos')
def step_given_user_is_on_food_section(context):
    """Given que el usuario está en la sección de alimentos"""
    # Lógica para ir a la sección de alimentos
    pass

@when('agrega {quantity:d} unidades de "{item_name}" al carrito')
def step_when_adds_quantity_of_item(context, quantity, item_name):
    """When agrega 101 unidades de "Palomitas de Maíz" al carrito"""
    # Lógica para simular la adición de unidades al carrito
    context.added_quantity = quantity
    pass

@when('la cantidad de "{item_name}" en el carrito es de {expected_quantity:d}')
def step_and_cart_quantity_is_expected(context, item_name, expected_quantity):
    """And la cantidad de "Palomitas de Maíz" en el carrito es de 101"""
    # Lógica para verificar la cantidad en el carrito
    # assert context.added_quantity == expected_quantity
    pass

@then('no se muestra ningún mensaje de error')
def step_then_no_error_message(context):
    """Then no se muestra ningún mensaje de error"""
    # Lógica para verificar que un elemento de error no está visible
    pass

# ---
# Feature: Indicador de interactividad para imágenes
# ---

def step_given_user_is_on_food_section_again(context):
    """Given que el usuario está en la sección de alimentos"""
    # Lógica para ir a la sección de alimentos
    pass

@when('mueve el cursor sobre la imagen de unas palomitas')
def step_when_hovers_over_popcorn_image(context):
    """When mueve el cursor sobre la imagen de unas palomitas"""
    # Lógica para simular el "hover" (mover el cursor sobre un elemento)
    # Por ejemplo, usando ActionChains de Selenium
    pass

@then('el cursor cambia de una flecha a una mano')
def step_then_cursor_changes_to_hand(context):
    """Then el cursor cambia de una flecha a una mano"""
    # Lógica para verificar el estilo del cursor (usando JavaScript o CSS)
    # assert context.driver.execute_script("return document.body.style.cursor;") == "pointer"
    pass

# ---
# Feature: Efecto visual interactivo en la cartelera
# ---

def step_given_user_is_on_home_page_again(context):
    """Given que el usuario está en la página de inicio"""
    # Lógica para ir a la página de inicio
    pass

@when('mueve el cursor sobre la imagen de una película')
def step_when_hovers_over_movie_image(context):
    """When mueve el cursor sobre la imagen de una película"""
    # Lógica para simular el "hover" sobre la imagen de una película
    pass

@then('la imagen se agranda para hacer zoom')
def step_then_image_zooms(context):
    """Then la imagen se agranda para hacer zoom"""
    # Lógica para verificar el cambio de tamaño del elemento (usando CSS o atributos de estilo)
    pass

# ---
# Feature: Efecto visual en la barra de navegación
# ---

@given('que el usuario está en la página de inicio')
def step_given_user_is_on_home_page_yet_again(context):
    """Given que el usuario está en la página de inicio"""
    # Lógica para ir a la página de inicio
    pass

@when('mueve el cursor sobre una opción de la barra de navegación, como "{option_name}"')
def step_when_hovers_over_nav_option(context, option_name):
    """When mueve el cursor sobre una opción de la barra de navegación, como "Películas" """
    # Lógica para simular el "hover" sobre la opción de navegación
    pass

@then('el texto de la opción cambia de color de blanco a azul')
def step_then_text_changes_color(context):
    """Then el texto de la opción cambia de color de blanco a azul"""
    # Lógica para verificar el color del texto del elemento
    # assert context.driver.find_element(By.LINK_TEXT, "Películas").value_of_css_property("color") == "rgba(0, 0, 255, 1)" # azul
    pass

# ---
# Feature: Añadir múltiples unidades al carrito
# ---

@given('que el usuario está en la sección de alimentos')
def step_given_user_is_on_food_section_and_empty_cart(context):
    """Given que el usuario está en la sección de alimentos"""
    # Lógica para ir a la sección de alimentos
    pass

@given('que el carrito de compras está vacío')
def step_and_shopping_cart_is_empty(context):
    """And que el carrito de compras está vacío"""
    # Lógica para vaciar el carrito o verificar que está vacío al inicio
    pass

@when('hago clic {times:d} veces en el botón "Agregar" para las "{item_name}"')
def step_when_clicks_add_button_multiple_times(context, times, item_name):
    """When hago clic 3 veces en el botón "Agregar" para las "Palomitas de Maíz" """
    # Lógica para hacer clic en el botón de agregar varias veces
    pass

@then('la cantidad de "{item_name}" en el carrito es {expected_quantity:d}')
def step_then_cart_quantity_is_expected_final(context, item_name, expected_quantity):
    """Then la cantidad de "Palomitas de Maíz" en el carrito es 3"""
    # Lógica para verificar la cantidad final en el carrito
    pass

# ---
# Feature: Restricción de promociones por día de la semana
# ---

@given('que la fecha actual es un día {day_of_week}')
def step_given_current_date_is_day(context, day_of_week):
    """Given que la fecha actual es un día jueves"""
    # Lógica para establecer o simular el día de la semana para la prueba
    # Por ejemplo, usar la librería datetime
    pass

@given('que el usuario está en la sección de "Promos"')
def step_and_user_is_on_promos_section(context):
    """And que el usuario está en la sección de "Promos" """
    # Lógica para navegar a la sección de promociones
    pass

@when('intenta comprar la promoción "{promo_name}"')
def step_when_tries_to_buy_promo(context, promo_name):
    """When intenta comprar la promoción "Miércoles 2x1" """
    # Lógica para hacer clic en el botón de comprar de la promoción
    pass

@when('el sistema muestra un mensaje de error')
def step_and_system_shows_error_message(context):
    """And el sistema muestra un mensaje de error"""
    # Lógica para verificar que el mensaje de error aparece
    pass

@then('el mensaje indica que la promoción no está disponible hoy')
def step_then_message_indicates_promo_not_available(context):
    """Then el mensaje indica que la promoción no está disponible hoy"""
    # Lógica para verificar el texto específico del mensaje de error
    pass

# ---
# Feature: Restricción de promociones con combos
# ---

@given('que el usuario está en la sección de "Promos"')
def step_given_user_is_on_promos_section_again(context):
    """Given que el usuario está en la sección de "Promos" """
    # Lógica para navegar a la sección de promociones
    pass

@given('que mi carrito de compras no contiene un combo')
def step_and_cart_does_not_contain_combo(context):
    """And que mi carrito de compras no contiene un combo"""
    # Lógica para verificar el contenido del carrito
    pass

@when('intenta agregar la "{item_name}" a mi carrito')
def step_when_tries_to_add_item(context, item_name):
    """When intenta agregar la "Bebida grande gratis" a mi carrito"""
    # Lógica para hacer clic en el botón de agregar la bebida
    pass

@then('el sistema muestra un mensaje de error')
def step_then_system_shows_error_message_again(context):
    """Then el sistema muestra un mensaje de error"""
    # Lógica para verificar que el mensaje de error es visible
    pass

@then('la cantidad de "{item_name}" en mi carrito es {quantity:d}')
def step_then_item_quantity_in_cart_is(context, item_name, quantity):
    """And la cantidad de "Bebida grande gratis" en mi carrito es 0"""
    # Lógica para verificar la cantidad final en el carrito
    pass