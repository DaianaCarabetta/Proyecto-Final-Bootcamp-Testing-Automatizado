Feature: Validar que la sección "Horarios" no tiene función asignada en la homepage
  Como usuario del sitio web de cine
  Quiero que la sección "Horarios" no tenga comportamiento activo si no está configurada
  Para evitar confusión o redirecciones inesperadas

  Background:
    Given que el usuario se encuentra en la página de inicio

  Scenario: Comprobar en la homepage que la sección "Horarios" no tiene asignada ninguna función
    When hace scroll en la cartelera
    And hace clic en la palabra "Horarios"
    Then no ocurre ninguna acción ni redirección

