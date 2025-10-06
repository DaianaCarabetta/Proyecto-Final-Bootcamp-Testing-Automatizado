@bug
Feature: Horarios diferentes en la selección de asiento
  Como usuario del sitio web del cine
  Quiero que la fecha y el horario que selecciono para una película se refleje correctamente
  Para evitar confusión y asegurar que estoy comprando boletos para el horario deseado

  Background:
    Given que el usuario está en la página de inicio
    When el usuario navega a la sección de cartelera
    And selecciona la película "Superman"
    Then debería ver el detalle de la película Superman
    When selecciona el día siguiente
    And selecciona un horario en Español

  Scenario: Validar que no se muestran horarios incorrectos al seleccionar una función distinta de las 9pm o 10pm
    Then el resumen de carrito debe reflejar la fecha y el horario seleccionado
    And no deben aparecer en Fecha y hora Hoy, 27 de julio, 10:00 pm


