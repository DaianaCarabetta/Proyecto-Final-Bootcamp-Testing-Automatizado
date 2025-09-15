Feature: Visualizar títulos de películas

  Como cliente del cine
  Quiero visualizar los títulos de las películas
  Para saber si me interesa verlas


  Scenario: Validar título inicial que coincida con el tema de la película 'Los 4 fantásticos'
    Given El usuario debe estar en el sitio https://fake-cinema.vercel.app/
    When El usuario ingresa a la opción peliculas
    Then Debe decir el título "Los mismos héroes, como antes" en plural

  Scenario: Comprobar que el usuario accede a la página principal correctamente
    Given que el usuario se encuentra en la página de inicio
    When el usuario navega a la URL del sitio web https://fake-cinema.vercel.app/
    And debería ver la página principal con la cartelera actual
    Then debería poder ver los títulos de las películas disponibles