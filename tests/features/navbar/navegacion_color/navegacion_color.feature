Feature: Efecto visual en la barra de navegación
  Como usuario del sitio web
  Quiero que las opciones de la barra de navegación cambien de color al pasar el cursor
  Para que me indiquen que son enlaces interactivos

  Background:
    Given que el usuario está en la página de inicio

  Scenario: Verificar que el texto de la navegación cambia de color al pasar el cursor
    When mueve el cursor sobre una opción de la barra de navegación, como "Películas"
    Then el texto de la opción cambia de color de blanco a azul