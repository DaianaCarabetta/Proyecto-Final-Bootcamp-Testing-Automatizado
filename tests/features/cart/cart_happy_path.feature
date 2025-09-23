Feature: Carrito de compras
  Como usuario del cine
  Quiero visualizar los productos en mi carrito
  Para confirmar mi compra antes del pago

  Background:
    Given el usuario accede a la vista de Alimentos
    When selecciona "Palomitas"
    And hace clic en "Agregar al carrito"
    And vuelve a la vista de Alimentos
    And selecciona "Hot Dog"
    And hace clic en "Agregar al carrito"
    And accede a la vista de Carrito

  Scenario: Ver items del carrito
    Then debería ver "Palomitas" con su precio "$3.50"
    And debería ver "Hot Dog" con su precio "$4.00"

  Scenario: Ver subtotal y total
    Then debería visualizar el subtotal "$7.50"
    And debería visualizar el total "$7.50"

  Scenario: Proceder al pago desde el carrito
    When hace clic en "Proceder al pago"
    Then el sistema debería redirigirlo a la vista de checkout

