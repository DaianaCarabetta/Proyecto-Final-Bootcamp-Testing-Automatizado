Feature: Efecto visual interactivo en la cartelera
  Como usuario del sitio web de cine
  Quiero que las imágenes de las películas se destaquen al pasar el cursor sobre ellas
  Para que sea más fácil ver los detalles de cada título

  Scenario: Comprobar que las imágenes de las películas hacen zoom al pasar el cursor
    Given que el usuario está en la página de inicio
    When mueve el cursor sobre la imagen de una película
    Then la imagen se agranda para hacer zoom