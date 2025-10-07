@bug
Feature: Validar la sección "Horarios"

  Background:
    Given que el usuario está en la página de inicio
    When el usuario navega a la sección de cartelera

  Scenario: Comprobar funcionalidad de la sección "Horarios"
    And hace clic en la palabra "Horarios"
    Then deberia mostrar la seccion de horarios
