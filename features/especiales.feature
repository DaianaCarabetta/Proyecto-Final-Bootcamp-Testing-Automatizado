Feature: Listado de Especiales

  Background:
    Given el usuario navega a "especiales"

  @smoke @ui
  Scenario: Se muestra el encabezado "Especiales"
    Then debería visualizar un encabezado con el texto "Especiales"

  @smoke @ui
  Scenario: Cada tarjeta muestra información mínima requerida
    Then debería visualizar al menos 1 tarjeta de especial
    And cada tarjeta debe mostrar un título no vacío
    And cada tarjeta debe mostrar una breve descripción no vacía

  @regression @ui
  Scenario: Las imágenes se muestran cuando aplica
    Then para las tarjetas que tengan imagen disponible
    And la imagen debe renderizarse correctamente
    And la imagen debe tener atributo alt no vacío

  @regression @data
  Scenario: Se cargan todos los especiales disponibles desde backend
    When la respuesta del backend contiene N especiales
    Then el listado en la UI debe mostrar exactamente N tarjetas

  @negative @defensive
  Scenario: Estado vacío cuando no hay especiales
    Given la respuesta del backend no contiene especiales
    Then debería mostrarse el mensaje "No hay especiales disponibles"
    And no deberían mostrarse tarjetas vacías ni errores visibles
