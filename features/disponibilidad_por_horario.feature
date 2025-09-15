Feature: Disponibilidad de funciones por horario
  Como usuario de la cartelera del cine
  Quiero que las funciones pasadas no se muestren
  Para evitar que intente comprar boletos para horarios ya no disponibles

  Scenario: Comprobar que la función de las 11:00 AM no está disponible después de su horario
    Given que son las 11:01 AM o más tarde
    And que el usuario está navegando en la cartelera de películas del sitio web
    When busca la película con la función de las 11:00 AM
    Then la opción para comprar boletos para la función de las 11:00 AM no se muestra