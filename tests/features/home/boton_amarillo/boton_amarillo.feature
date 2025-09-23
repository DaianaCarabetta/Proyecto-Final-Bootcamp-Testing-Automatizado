Feature: Validar que el botón no cambia a color negro al pasar el cursor sobre la clasificación

  Scenario: Verificar que el botón no cambie a color negro al pasar el cursor sobre la clasificación
    Given que estoy en la interfaz de programación de películas
    When hay una película con clasificación visible (por ejemplo, "B")
    And paso el cursor sobre la clasificación de la película
    And el botón relacionado no debe cambiar a color negro
    Then el botón relacionado no debe cambiar a color negro