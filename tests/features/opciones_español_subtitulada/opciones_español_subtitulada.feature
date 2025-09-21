Feature: Persistencia de opciones de idioma al refrescar la interfaz

  Scenario: Verificar que las opciones "Español" y "Subtitulada" se mantengan al presionar el botón Refrescar
    Given que una película está programada con las opciones de idioma "Español" y "Subtitulada"
    When estas opciones son visibles en la interfaz de programación
    And presiono el botón "Refrescar"
    And las opciones de idioma "Español" y "Subtitulada" deben permanecer visibles
    Then no deben desaparecer ni cambiar aleatoriamente
