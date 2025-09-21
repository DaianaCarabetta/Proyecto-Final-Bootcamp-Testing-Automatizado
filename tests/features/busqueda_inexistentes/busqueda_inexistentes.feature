Feature: Búsqueda de películas inexistentes
  Como usuario del sitio web de cine
  Quiero que la búsqueda de películas sea precisa
  Para no encontrar títulos que no están disponibles o que no existen

  Scenario: Validar que la película "Sonic 3" no se muestra en la cartelera
    Given que el usuario está en la página de inicio del sitio web del cine
    When busca la película con el título "Sonic 3"
    Then no se muestran resultados para la película "Sonic 3"