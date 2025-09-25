Feature: Restricción de promociones con combos
  Como usuario del sitio web de cine
  Quiero que la promoción de bebida gratis solo esté disponible con la compra de un combo
  Para evitar errores en mi pedido y en la lógica de negocio

  Background:
    Given que el usuario está en la sección de "Promos"
    And que mi carrito de compras no contiene un combo

  Scenario: Corroborar que no se puede agregar una bebida gratis al carrito sin un combo
    When intenta agregar la "Bebida grande gratis" a mi carrito
    Then el sistema muestra un mensaje de error
    And la cantidad de "Bebida grande gratis" en mi carrito es 0