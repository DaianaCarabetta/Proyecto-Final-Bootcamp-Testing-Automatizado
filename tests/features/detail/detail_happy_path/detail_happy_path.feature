Feature: Detalle de película
  Como usuario
  Quiero ver la información de la película y reservar entradas
  Para poder seleccionar un asiento en una función

  Background:
    Given que el usuario está en la página de inicio
    When el usuario navega a la sección de cartelera
    And selecciona la película "Superman"

  Scenario: Selección de función en español para mañana
    Then debería ver el detalle de la película Superman
    When selecciona el día siguiente
    And selecciona un horario en Español
    Then el sistema lo redirige a la página de selección de asientos
