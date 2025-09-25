Feature: Visualizar títulos de películas
  Como cliente del cine
  Quiero visualizar los títulos de las películas
  Para saber si me interesa verlas

  Background:
    Given que el usuario está en el sitio https://fake-cinema.vercel.app/

  Scenario: Validar título inicial que coincida con el tema de la película 'Los 4 fantásticos'
    When el usuario ingresa a la opción peliculas
    Then debe decir el título "Los mismos héroes, como antes" en plural

  Scenario: Comprobar que el usuario accede a la página principal correctamente
    When el usuario navega a la URL del sitio web https://fake-cinema.vercel.app/
    And debería ver la página principal con la cartelera actual
    Then debería poder ver los títulos de las películas disponibles