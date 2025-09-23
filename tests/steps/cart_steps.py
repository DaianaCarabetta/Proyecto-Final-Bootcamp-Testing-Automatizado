from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.cart_page  import CartPage

URL_ALIMENTOS = "https://fake-cinema.vercel.app/alimentos"
URL_CHECKOUT = "https://fake-cinema.vercel.app/checkout"


@given('el usuario accede a la vista de Alimentos')
def step_impl(context):
    context.driver.get(URL_ALIMENTOS)
    WebDriverWait(context.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h3[text()='Palomitas']"))
    )


@when('selecciona "Palomitas"')
def step_impl(context):
    palomitas = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//h3[text()='Palomitas']"))
    )
    palomitas.click()


@when('hace clic en "Agregar al carrito"')
def step_impl(context):
    boton = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Agregar al carrito')]"))
    )
    boton.click()


@when('vuelve a la vista de Alimentos')
def step_impl(context):
    alimentos = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Alimentos')]"))
    )
    alimentos.click()


@when('selecciona "Hot Dog"')
def step_impl(context):
    hotdog = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//h3[text()='Hot Dog']"))
    )
    hotdog.click()


@when('accede a la vista de Carrito')
def step_impl(context):
    carrito = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Carrito')]"))
    )
    carrito.click()


@then('debería ver "Palomitas" con su precio "$3.50"')
def step_impl(context):
    cart_page = CartPage(context.driver)
    assert cart_page.is_item_displayed("Palomitas", "$3.50")


@then('debería ver "Hot Dog" con su precio "$4.00"')
def step_impl(context):
    cart_page = CartPage(context.driver)
    assert cart_page.is_item_displayed("Hot Dog", "$4.00")


@then('debería visualizar el subtotal "$7.50"')
def step_impl(context):
    cart_page = CartPage(context.driver)
    assert cart_page.get_subtotal() == "$7.50"


@then('debería visualizar el total "$7.50"')
def step_impl(context):
    cart_page = CartPage(context.driver)
    assert cart_page.get_total() == "$7.50"


@when('hace clic en "Proceder al pago"')
def step_impl(context):
    cart_page = CartPage(context.driver)
    cart_page.click_checkout()


@then('el sistema debería redirigirlo a la vista de checkout')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        EC.url_contains("checkout")
    )
    assert context.driver.current_url == URL_CHECKOUT
