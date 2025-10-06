Feature: Selección de asientos y compra de boletos
  Como usuario
  Quiero seleccionar un asiento y comprar boletos
  Para confirmar mi reserva en el carrito

  Background:
    Given que el usuario está en la página de inicio
    When el usuario navega a la sección de cartelera
    And selecciona la película "Superman"
    Then debería ver el detalle de la película Superman
    When selecciona el día siguiente
    And selecciona un horario en Español
    Then el sistema lo redirige a la página de selección de asientos


  Scenario: Compra de un boleto adulto con asiento seleccionado
    When el usuario selecciona el asiento "G5"
    And hace clic en "Comprar boletos"
    And en el modal ingresa "1" en Adultos
    And confirma la selección
    Then el sistema lo redirige al carrito


