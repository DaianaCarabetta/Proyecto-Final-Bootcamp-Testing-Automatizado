@bug
Feature: Redirección al seleccionar el Combo Pareja

  Scenario: Verificar que al seleccionar el "Combo Pareja" se redirige primero a la selección de asientos
    Given que estoy en la pantalla de Promos
    When el Combo Pareja está disponible
    And selecciono el Combo Pareja
    And agrego el Combo Pareja al carrito
    Then el sistema debe redirigirme a la pantalla de selección de asientos
    And debe redirigirme a la pantalla de pago

