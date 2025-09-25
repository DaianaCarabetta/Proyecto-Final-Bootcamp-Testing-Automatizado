Feature: Validar que el botón no cambia a color negro al pasar el cursor sobre la clasificación
  Como usuario del sitio web del cine
  Quiero que los botones mantengan su estilo al interactuar con elementos como la clasificación
  Para evitar confusión visual y asegurar una experiencia coherente

  Background:
    Given que estoy en la interfaz de programación de películas

  Scenario: Verificar que el botón no cambie a color negro al pasar el cursor sobre la clasificación
    When hay una película con clasificación visible (por ejemplo, "B")
    And paso el cursor sobre la clasificación de la película
    Then el botón relacionado no debe cambiar a color negro