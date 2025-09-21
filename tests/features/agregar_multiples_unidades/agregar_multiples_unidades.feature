Feature: Añadir múltiples unidades al carrito
  Como usuario de la sección de alimentos
  Quiero que la cantidad de un producto se incremente al agregarlo varias veces
  Para que me sea fácil comprar múltiples unidades de un mismo artículo

  Scenario: Corroborar que la cantidad de palomitas aumenta en el carrito al hacer clic varias veces
    Given que el usuario está en la sección de alimentos
    When hago clic 3 veces en el botón "Agregar" para las "Palomitas de Maíz"
    Then la cantidad de "Palomitas de Maíz" en el carrito es 3