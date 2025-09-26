# features/steps/especiales_steps.py
from behave import given, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@given('el usuario navega a "{ruta}"')
def step_go_to_section(context, ruta):
    # Usa la base_url definida en features/environment.py
    context.driver.get(f"{context.base_url}/{ruta}")

@then('debería visualizar un encabezado con el texto "{texto}"')
def step_see_header_with_text(context, texto):
    wait = WebDriverWait(context.driver, 10)

    # Intentamos primero h1/h2; si no, cualquier elemento con role="heading"
    locators = [
        (By.XPATH, f"//*[self::h1 or self::h2][contains(normalize-space(.), '{texto}')]"),
        (By.XPATH, f"//*[@role='heading' and contains(normalize-space(.), '{texto}')]"),
    ]

    el = None
    for locator in locators:
        try:
            el = wait.until(EC.visibility_of_element_located(locator))
            break
        except TimeoutException:
            continue

    assert el is not None, f'No se encontró un encabezado visible con el texto "{texto}".'
