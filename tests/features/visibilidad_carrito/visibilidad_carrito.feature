Feature: Visibilidad de alimentos en el carrito
  Como usuario del sitio de venta de boletos
  Quiero que mi selección de alimentos sea visible durante todo el proceso de compra
  Para no olvidar lo que agregué y saber el total de mi pedido

  Background:
    Given que el usuario ha agregado palomitas de maíz al carrito
    And que ha seleccionado un boleto de cine para una película

  Scenario: Validar que el alimento seleccionado permanece visible al escoger un asiento
    When avanza a la sección de selección de asiento
    Then mi carrito de compras muestra las palomitas de maíz seleccionadas
