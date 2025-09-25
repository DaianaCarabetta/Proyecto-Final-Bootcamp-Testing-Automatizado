Feature: Indicador de interactividad para imágenes
  Como usuario del sitio web de cine
  Quiero que el cursor cambie al pasar sobre imágenes clicables
  Para saber que puedo interactuar con ellas

  Background:
    Given que el usuario está en la sección de alimentos

  Scenario: Comprobar que el cursor cambia a mano sobre las imágenes de los alimentos
    When mueve el cursor sobre la imagen de unas palomitas
    Then el cursor cambia de una flecha a una mano