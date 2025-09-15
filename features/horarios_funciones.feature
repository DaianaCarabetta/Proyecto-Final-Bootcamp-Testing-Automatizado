Feature: Estabilidad de los horarios de funciones
  Como usuario de la aplicación de cine
  Quiero que los horarios de las funciones sean consistentes
  Para poder planificar mi visita al cine sin confusiones

Scenario: El sistema impide programar funciones que se superponen
  Given que la duración de la película es de 140 minutos
  And existe una función programada en la Sala 1 a las 14:00
  When intento programar una nueva función en la Sala 1 a las 14:30
  Then el sistema muestra un mensaje de error indicando superposición de horarios
  Then no permite guardar la nueva función

Scenario: Verificar que los horarios no cambien aleatoriamente al presionar el botón Refrescar
    Given que el usuario tiene una lista de funciones de películas con horarios previamente programados
    When hace clic en la película Superman
    And los horarios están correctamente asignados y visibles en la interfaz
    And presiona el botón "Refrescar"
    And los horarios de las funciones deben mantenerse sin cambios
    Then no deben generarse horarios aleatorios