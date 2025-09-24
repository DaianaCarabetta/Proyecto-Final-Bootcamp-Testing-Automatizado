Feature: Persistencia de opciones de idioma al refrescar la interfaz
  Como usuario del sitio web del cine
  Quiero que las opciones de idioma se mantengan visibles al refrescar la interfaz
  Para evitar confusión y asegurar que las funciones se mantengan configuradas correctamente

  Background:
    Given que una película está programada con las opciones de idioma "Español" y "Subtitulada"

  Scenario: Verificar que las opciones "Español" y "Subtitulada" se mantengan al presionar el botón Refrescar
    When estas opciones son visibles en la interfaz de programación
    And presiono el botón "Refrescar"
    And las opciones de idioma "Español" y "Subtitulada" deben permanecer visibles
    Then no deben desaparecer ni cambiar aleatoriamente
