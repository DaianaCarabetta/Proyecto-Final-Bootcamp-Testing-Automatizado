Feature: Límite en la cantidad de productos
  Como usuario que compra alimentos
  Quiero poder agregar una cantidad ilimitada de un producto
  Para poder comprar para un grupo grande de personas sin restricciones

  Scenario: Comprobar que un usuario puede agregar más de 100 unidades de un alimento al carrito
    Given que el usuario está en la sección de alimentos
    When agrega 101 unidades de "Palomitas de Maíz" al carrito
    And la cantidad de "Palomitas de Maíz" en el carrito es de 101
    Then no se muestra ningún mensaje de error