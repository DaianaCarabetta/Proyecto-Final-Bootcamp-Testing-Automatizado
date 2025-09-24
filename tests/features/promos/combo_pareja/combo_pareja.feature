Feature: Redirección al seleccionar el Combo Pareja
  Como usuario del sitio de venta de boletos
  Quiero que al seleccionar el combo "Pareja" se me redirija primero a la selección de sillas
  Para poder elegir mi ubicación antes de pagar y asegurar una experiencia cómoda

  Background:
    Given que estoy en la pantalla de selección de Promos
    And el combo "Pareja" está disponible

  Scenario: Verificar que al seleccionar el "Combo Pareja" se redirige primero a la selección de sillas
    When selecciono el combo "Pareja"
    And el sistema debe redirigirme a la pantalla de selección de sillas
    Then después de seleccionar las sillas, debe redirigirme a la pantalla de pago
