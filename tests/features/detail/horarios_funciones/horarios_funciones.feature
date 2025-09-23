Feature: Estabilidad de los horarios de funciones
  Como usuario de la aplicación de cine
  Quiero que los horarios de las funciones sean consistentes
  Para poder planificar mi visita al cine sin confusiones

Scenario: Validar superposición entre funciones en programación de películas
  Given que la duración de la película es de 140 minutos
  And existe una función programada en la Sala 1 a las 14:00
  When intento programar una nueva función en la Sala 1 a las 14:30
  Then el sistema muestra un mensaje de error indicando superposición de horarios
  Then no permite guardar la nueva función

Scenario: Verificar que los horarios no cambien aleatoriamente al presionar el botón Refrescar
    Given que el usuario está en la página de detalles de una película
    And que la página ha cargado la lista de horarios de las funciones
    When hace clic en la película Superman
    Then la lista de horarios de las funciones sigue siendo la misma