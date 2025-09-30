Feature: Home - Happy Path
  Como usuario del sitio web de cine
  Quiero navegar desde la página de inicio
  Para poder acceder a la cartelera y detalles de una película

  Background:
    Given que el usuario está en la página de inicio

  Scenario: Navegar el carrusel y acceder a detalle de película
    When el carrusel de películas se ha cargado correctamente
    And presiona el botón de la flecha derecha del carrusel
    Then el carrusel muestra una película disponible

    When el usuario navega a la sección de cartelera
    Then debería ver los títulos de las películas disponibles

    When selecciona la película "Superman"
    Then el sistema lo redirige al detalle de la película Superman
