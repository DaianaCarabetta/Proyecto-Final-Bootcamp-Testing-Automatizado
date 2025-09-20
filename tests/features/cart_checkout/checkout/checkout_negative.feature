@bug
Feature: Checkout - Casos Negativos
  Como usuario
  Quiero que los campos del formulario de checkout validen los datos correctamente
  Para evitar errores en el proceso de pago

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

  Scenario: Validación del nombre de tarjeta
    Given el usuario está en la vista de checkout
    When ingresa números en el campo "Nombre en la tarjeta"
    Then el sistema debería mostrar un error indicando que solo se permiten letras
    And el botón de confirmación de pago debería estar deshabilitado

  Scenario: Validación en el número de tarjeta
    Given el usuario está en la vista de checkout
    When ingresa texto en el campo "Número de tarjeta"
    Then el sistema debería mostrar un error indicando que solo se permiten números
    And el botón de confirmación de pago debería estar deshabilitado

  Scenario: Validación del CVV
    Given el usuario está en la vista de checkout
    When ingresa texto en el campo "CVV"
    Then el sistema debería mostrar un error indicando que solo se permiten números de 3 o 4 dígitos
    And el botón de confirmación de pago debería estar deshabilitado
