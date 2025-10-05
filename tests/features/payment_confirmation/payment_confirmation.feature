Feature: Confirmación de pago
  Como usuario
  Quiero visualizar la confirmación de mi compra
  Para tener certeza de que mi pago fue procesado correctamente

  Background:
    Given el usuario accede a la vista de Alimentos
    When selecciona "Palomitas"
    And hace clic en "Agregar al carrito"
    And vuelve a la vista de Alimentos
    And selecciona "Hot Dog"
    And hace clic en "Agregar al carrito"
    And accede a la vista de Carrito
    And hace clic en "Proceder al pago"
    And el usuario completó el formulario de checkout con datos válidos y confirmó el pago

  Scenario: Visualizar resumen de compra en confirmación
    Then se muestra la vista de confirmación de pago
    And debería visualizar un resumen de la compra con los productos adquiridos y el detalle
    And debería visualizar el monto total de la compra
    And debería visualizar un número de compra único

  Scenario: Volver al inicio desde confirmación
    Given el usuario está en la vista de confirmación de pago
    When hace clic en el botón "Volver al inicio"
    Then el sistema debería redirigirlo a la página de inicio

