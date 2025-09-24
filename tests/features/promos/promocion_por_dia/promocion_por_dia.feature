Feature: Restricción de promociones por día de la semana
  Como usuario que quiere aprovechar una promoción
  Quiero que el sistema valide el día de la semana para una oferta
  Para evitar que intente comprar promociones que no están activas

  Background:
    Given que la fecha actual es un día jueves
    And que el usuario está en la sección de "Promos"

  Scenario: Comprobar que la promoción de 2x1 no está disponible un jueves
    When intenta comprar la promoción "Miércoles 2x1"
    And el sistema muestra un mensaje de error
    Then el mensaje indica que la promoción no está disponible hoy
