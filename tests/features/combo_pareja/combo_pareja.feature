Feature: Redirección al seleccionar el Combo Pareja

  Scenario: Verificar que al seleccionar el "Combo Pareja" se redirige primero a la selección de sillas
    Given que estoy en la pantalla de selección de Promos
    When el combo "Pareja" está disponible
    And selecciono el combo "Pareja"
    And el sistema debe redirigirme a la pantalla de selección de sillas
    Then después de seleccionar las sillas, debe redirigirme a la pantalla de pago
