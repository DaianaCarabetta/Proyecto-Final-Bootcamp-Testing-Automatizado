Feature: Validar que la sección "Horarios" no tiene función asignada en la homepage

  Scenario: Comprobar en la homepage que la sección "Horarios" no tiene asignada ninguna función
    Given que el usuario se encuentra en la página de inicio
    When hace scroll en la cartelera
    And hace clic en la palabra "Horarios"
    Then no ocurre ninguna acción ni redirección
