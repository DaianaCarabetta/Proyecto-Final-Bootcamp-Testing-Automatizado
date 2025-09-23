Feature: Checkout
  Como usuario
  Quiero poder realizar el proceso de checkout correctamente
  Para finalizar mi compra de manera exitosa

  Background:
    Given el usuario accede a la vista de Alimentos
    When selecciona "Palomitas"
    And hace clic en "Agregar al carrito"
    And vuelve a la vista de Alimentos
    And selecciona "Hot Dog"
    And hace clic en "Agregar al carrito"
    And accede a la vista de Carrito
    And hace clic en "Proceder al pago"
    Then el sistema debería redirigirlo a la vista de checkout


  Scenario: Visualizar resumen de compra en checkout
    Then debería visualizar la lista de productos seleccionados con su precio unitario
    And debería visualizar el total de la compra


  Scenario: Validación de email en el formulario de checkout
    When intenta confirmar con un email inválido
    Then el sistema debe mostrar un mensaje de error


  Scenario: Validación de campos obligatorios
    When deja vacío el campo "Apellido"
    Then el sistema debe mostrar un mensaje de error indicando que el campo es obligatorio


  Scenario: Completar checkout y redirigir a confirmación de pago
    When el usuario completó el formulario de checkout con datos válidos y confirmó el pago
    Then el sistema debería redirigirlo a la vista de confirmación de pago
