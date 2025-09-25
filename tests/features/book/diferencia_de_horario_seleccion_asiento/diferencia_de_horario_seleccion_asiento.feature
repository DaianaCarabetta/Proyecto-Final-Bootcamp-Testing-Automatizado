Feature: Horarios diferentes en la selección de asiento
  Como usuario del sitio web del cine
  Quiero que el horario que selecciono para una película se refleje correctamente en la página de selección de asiento
  Para evitar confusión y asegurar que estoy comprando boletos para el horario deseado

  Background:
    Given que el usuario está en la cartelera de películas

  Scenario: Validar que no se muestran horarios incorrectos al seleccionar una función distinta de las 9pm o 10pm
    And selecciona una función con horario AM o PM distinto de las 21:00 o 22:00
    When accede a la página de selección de asiento
    And no deben aparecer los horarios de las 21:00 ni 22:00 en el lado izquierdo
    Then debe mostrarse únicamente el horario seleccionado por el usuario