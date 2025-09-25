Feature: Navegación del carrusel de películas
  Como usuario del sitio web de cine
  Quiero poder navegar entre las películas del carrusel
  Para ver la cartelera de forma intuitiva

  Background:
    Given que el usuario está en la página de inicio
    And que el carrusel de películas se ha cargado correctamente

  Scenario: Validar que se avanza a la siguiente película en el carrusel
    When presiona el botón de la flecha derecha del carrusel
    And la siguiente película en el carrusel se vuelve visible
    Then el carrusel muestra la película "Superman"