@e2e
Feature: Flujo E2E de compra completa
  Como usuario
  Quiero realizar una compra completa de boletos
  Para verificar que el flujo funciona correctamente de principio a fin

  Scenario: Compra completa desde el Home hasta la confirmación de pago
    Given que el usuario está en la página de inicio
    When el carrusel de películas se ha cargado correctamente
    And presiona el botón de la flecha derecha del carrusel
    And el usuario navega a la sección de cartelera
    And selecciona la película Superman
    And selecciona el día siguiente
    And selecciona un horario en Español
    And el usuario selecciona el asiento "G5"
    And hace clic en "Comprar boletos"
    And en el modal ingresa "1" en Adultos
    And confirma la selección
    Then el sistema lo redirige al carrito

    When hace clic en "Proceder al pago"
    Then el sistema debería redirigirlo a la vista de checkout

    When el usuario completó el formulario de checkout con datos válidos y confirmó el pago
    Then se muestra la vista de confirmación de pago
    And debería visualizar un resumen de la compra con los productos adquiridos y el detalle
    And debería visualizar el monto total de la compra
    And debería visualizar un número de compra único

    When hace clic en el botón "Volver al inicio"
    Then el sistema debería redirigirlo a la página de inicio
