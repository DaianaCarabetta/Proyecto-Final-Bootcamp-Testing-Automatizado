#Exploración de funcionalidades que deberían existir pero no están implementadas
@bug
Feature: Carrito - Casos Negativos
  Como usuario
  Quiero poder administrar los productos en mi carrito
  Para tener control sobre mi compra antes del pago

  Background:
    Given el usuario accede a la vista de Alimentos
    When selecciona "Palomitas"
    And hace clic en "Agregar al carrito"
    And vuelve a la vista de Alimentos
    And selecciona "Hot Dog"
    And hace clic en "Agregar al carrito"
    And accede a la vista de Carrito

  Scenario: Eliminar un producto del carrito
    Given el usuario tiene productos en el carrito
    When intenta eliminar un producto del carrito
    Then debería existir un botón o acción para eliminarlo

  Scenario: Incrementar cantidad de un producto
    Given el usuario tiene productos en el carrito
    When quiere aumentar la cantidad de un producto
    Then debería existir un botón o control para incrementarla

  Scenario: Disminuir cantidad de un producto
    Given el usuario tiene productos en el carrito
    When quiere disminuir la cantidad de un producto
    Then debería existir un botón o control para reducirla
