Feature: Disponibilidad de horarios después del cierre
  Como usuario del sitio web del cine
  Quiero que la cartelera refleje la disponibilidad real de horarios
  Para evitar la frustración de buscar funciones que ya no están disponibles

  Scenario: Verificar que los horarios para el día actual no se muestran después de las 23:00
    Given que son las 23:01 o más tarde, hora local
    And que el usuario está en la página de detalles de una película
    When revisa los horarios de las funciones para el día de hoy
    Then no se muestran horarios disponibles para el día actual