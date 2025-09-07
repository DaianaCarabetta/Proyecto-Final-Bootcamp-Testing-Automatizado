Feature: Visualizar títulos de películas

  Como cliente del cine
  Quiero visualizar los títulos de las películas
  Para saber si me interesa verlas


  Scenario: Validar título inicial que coincida con el tema de la película "Los 4 fantásticos"
    Given El usuario debe estar en el sitio https://fake-cinema.vercel.app/
    When El usuario ingresa a la opción películas
    Then Debe decir el título "Los mismos héroes, como antes" en plural

  Scenario: Comprobar que el usuario accede a la página principal correctamente
    Given que el usuario se encuentra en la página de inicio
    When el usuario navega a la URL del sitio web https://fake-cinema.vercel.app/
    And debería ver la página principal con la cartelera actual
    Then debería poder ver los títulos de las películas disponibles

  Scenario: Validar superposición entre funciones en programación de películas
    Given que la duración de la película es de 140 minutos
    When la sala se habilita cada 30 minutos para nuevas funciones
    And existe una función programada en la Sala 1 a las 14:00
    And intento programar una nueva función en la Sala 1 a las 14:30
    And el sistema debe mostrar un mensaje de error indicando superposición de horarios
    Then no debe permitir guardar la nueva función


Feature: Estabilidad de los horarios de funciones
  Como usuario de la aplicación de cine
  Quiero que los horarios de las funciones sean consistentes
  Para poder planificar mi visita al cine sin confusiones

  Scenario: Verificar que los horarios no cambien aleatoriamente al presionar el botón Refrescar
    Given que el usuario tiene una lista de funciones de películas con horarios previamente programados
    When hace clic en la película Superman
    And los horarios están correctamente asignados y visibles en la interfaz
    And presiona el botón "Refrescar"
    And los horarios de las funciones deben mantenerse sin cambios
    Then no deben generarse horarios aleatorios


Feature: Disponibilidad de funciones por horario
  Como usuario de la cartelera del cine
  Quiero que las funciones pasadas no se muestren
  Para evitar que intente comprar boletos para horarios ya no disponibles

  Scenario: Comprobar que la función de las 11:00 AM no está disponible después de su horario
    Given que son las 11:01 AM o más tarde
    And que el usuario está navegando en la cartelera de películas del sitio web
    When busca la película con la función de las 11:00 AM
    Then la opción para comprar boletos para la función de las 11:00 AM no se muestra


Feature: Disponibilidad de horarios después del cierre
  Como usuario del sitio web del cine
  Quiero que la cartelera refleje la disponibilidad real de horarios
  Para evitar la frustración de buscar funciones que ya no están disponibles

  Scenario: Verificar que los horarios para el día actual no se muestran después de las 23:00
    Given que son las 23:01 o más tarde, hora local
    And que el usuario está en la página de detalles de una película
    When revisa los horarios de las funciones para el día de hoy
    Then no se muestran horarios disponibles para el día actual


Feature: Búsqueda de películas inexistentes
  Como usuario del sitio web de cine
  Quiero que la búsqueda de películas sea precisa
  Para no encontrar títulos que no están disponibles o que no existen

  Scenario: Validar que la película "Sonic 3" no se muestra en la cartelera
    Given que el usuario está en la página de inicio del sitio web del cine
    When busca la película con el título "Sonic 3"
    Then no se muestran resultados para la película "Sonic 3"


Feature: Navegación del carrusel de películas
  Como usuario del sitio web de cine
  Quiero poder navegar entre las películas del carrusel
  Para ver la cartelera de forma intuitiva

  Scenario: Validar que se avanza a la siguiente película en el carrusel
    Given que el usuario está en la página de inicio
    And que el carrusel de películas se ha cargado correctamente
    When presiona el botón de la flecha derecha del carrusel
    And la siguiente película en el carrusel se vuelve visible
    Then el carrusel muestra la película "Superman"


Feature: Visibilidad del carrito de alimentos
  Como usuario del sitio de venta de boletos
  Quiero que mi selección de alimentos sea visible durante todo el proceso de compra
  Para no olvidar lo que agregué y saber el total de mi pedido

  Scenario: Validar que el alimento seleccionado permanece visible al escoger un asiento
    Given que el usuario ha agregado palomitas de maíz al carrito
    And que ha seleccionado un boleto de cine para una película
    When avanza a la sección de selección de asiento
    Then mi carrito de compras muestra las palomitas de maíz seleccionadas


Feature: Límite en la cantidad de productos
  Como usuario que compra alimentos
  Quiero poder agregar una cantidad ilimitada de un producto
  Para poder comprar para un grupo grande de personas sin restricciones

  Scenario: Comprobar que un usuario puede agregar más de 100 unidades de un alimento al carrito
    Given que el usuario está en la sección de alimentos
    When agrega 101 unidades de "Palomitas de Maíz" al carrito
    And la cantidad de "Palomitas de Maíz" en el carrito es de 101
    Then no se muestra ningún mensaje de error


Feature: Indicador de interactividad para imágenes
  Como usuario del sitio web de cine
  Quiero que el cursor cambie al pasar sobre imágenes clicables
  Para saber que puedo interactuar con ellas

  Scenario: Comprobar que el cursor cambia a mano sobre las imágenes de los alimentos
    Given que el usuario está en la sección de alimentos
    When mueve el cursor sobre la imagen de unas palomitas
    Then el cursor cambia de una flecha a una mano


Feature: Efecto visual interactivo en la cartelera
  Como usuario del sitio web de cine
  Quiero que las imágenes de las películas se destaquen al pasar el cursor sobre ellas
  Para que sea más fácil ver los detalles de cada título

  Scenario: Comprobar que las imágenes de las películas hacen zoom al pasar el cursor
    Given que el usuario está en la página de inicio
    When mueve el cursor sobre la imagen de una película
    Then la imagen se agranda para hacer zoom


Feature: Efecto visual en la barra de navegación
  Como usuario del sitio web
  Quiero que las opciones de la barra de navegación cambien de color al pasar el cursor
  Para que me indiquen que son enlaces interactivos

  Scenario: Verificar que el texto de la navegación cambia de color al pasar el cursor
    Given que el usuario está en la página de inicio
    When mueve el cursor sobre una opción de la barra de navegación, como "Películas"
    Then el texto de la opción cambia de color de blanco a azul


Feature: Añadir múltiples unidades al carrito
  Como usuario de la sección de alimentos
  Quiero que la cantidad de un producto se incremente al agregarlo varias veces
  Para que me sea fácil comprar múltiples unidades de un mismo artículo

  Scenario: Corroborar que la cantidad de palomitas aumenta en el carrito al hacer clic varias veces
    Given que el usuario está en la sección de alimentos
    And que el carrito de compras está vacío
    When hago clic 3 veces en el botón "Agregar" para las "Palomitas de Maíz"
    Then la cantidad de "Palomitas de Maíz" en el carrito es 3


Feature: Restricción de promociones por día de la semana
  Como usuario que quiere aprovechar una promoción
  Quiero que el sistema valide el día de la semana para una oferta
  Para evitar que intente comprar promociones que no están activas

  Scenario: Comprobar que la promoción de 2x1 no está disponible un jueves
    Given que la fecha actual es un día jueves
    And que el usuario está en la sección de "Promos"
    When intenta comprar la promoción "Miércoles 2x1"
    And el sistema muestra un mensaje de error
    Then el mensaje indica que la promoción no está disponible hoy


Feature: Restricción de promociones con combos
  Como usuario del sitio web de cine
  Quiero que la promoción de bebida gratis solo esté disponible con la compra de un combo
  Para evitar errores en mi pedido y en la lógica de negocio

  Scenario: Corroborar que no se puede agregar una bebida gratis al carrito sin un combo
    Given que el usuario está en la sección de "Promos"
    And que mi carrito de compras no contiene un combo
    When intenta agregar la "Bebida grande gratis" a mi carrito
    Then el sistema muestra un mensaje de error
    And la cantidad de "Bebida grande gratis" en mi carrito es 0