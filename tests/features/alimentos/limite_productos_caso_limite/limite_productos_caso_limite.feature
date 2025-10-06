@bug @caso_limite
Feature: Límite en la cantidad de productos
  Como usuario que compra alimentos
  Quiero que exista un límite razonable en la cantidad de un producto
  Para evitar errores o compras accidentales excesivas

  Scenario: Comprobar que un usuario no puede agregar más de 100 unidades de un alimento al carrito
    Given que el usuario está en la sección de alimentos
    When agrega 101 unidades de "Palomitas" al carrito
    Then se muestra un mensaje de error indicando que se alcanzó el límite máximo permitido
