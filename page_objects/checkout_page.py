from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    TITLE = (By.XPATH, "//h1[text()='Checkout']")
    PRODUCT_LIST = (By.CSS_SELECTOR, "main div.flex.justify-between.border-b")
    TOTAL = (By.CSS_SELECTOR, "div.flex.justify-between.font-bold span:last-child")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(., 'Confirmar pago')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(),'compra')]")

    INPUT_FIRSTNAME = (By.ID, "firstName")
    INPUT_LASTNAME = (By.ID, "lastName")
    INPUT_EMAIL = (By.ID, "email")
    INPUT_CARDNAME = (By.ID, "cardName")
    INPUT_CARDNUMBER = (By.ID, "cardNumber")
    INPUT_CVV = (By.ID, "cvv")


    def is_loaded(self):
        """Verifica que estemos en Checkout"""
        try:
            self.wait.until(EC.presence_of_element_located(self.TITLE))
            return True
        except TimeoutException:
            return False

    def is_item_displayed(self, nombre_producto, precio):
        """Verifica que un producto con precio aparezca en el resumen"""
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_LIST))
        productos = self.driver.find_elements(*self.PRODUCT_LIST)
        for producto in productos:
            texto = producto.text
            if nombre_producto in texto and precio in texto:
                return True
        return False

    def get_total(self):
        """Obtiene el total de la compra"""
        return self.wait.until(EC.presence_of_element_located(self.TOTAL)).text

    def fill_form(self, nombre, apellido, email, card_name, card_number, cvv):
        """Completa el formulario con los datos dados"""
        self.fill_field("firstName", nombre)
        self.fill_field("lastName", apellido)
        self.fill_field("email", email)
        self.fill_field("cardName", card_name)
        self.fill_field("cardNumber", card_number)
        self.fill_field("cvv", cvv)

    def confirm_payment(self):
        """Hace clic en Confirmar pago y espera redirección"""
        boton = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
        boton.click()
        from page_objects.payment_confirmation_page import ConfirmationPage
        return ConfirmationPage(self.driver)

    def get_success_message(self):
        """Devuelve el mensaje de compra exitosa"""
        try:
            return self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE)).text
        except TimeoutException:
            return None

    def get_field_validation_message(self, field_id):
        """Devuelve el mensaje de validación HTML5 que genera el navegador"""
        field = self.driver.find_element(By.ID, field_id)
        return field.get_attribute("validationMessage")

    def is_confirm_button_enabled(self):
        """Verifica si el botón de confirmar está habilitado"""
        boton = self.wait.until(EC.presence_of_element_located(self.CONFIRM_BUTTON))
        return boton.is_enabled()

    def fill_field(self, field_id, value):
        """Completa un input específico con el valor dado"""
        field = self.wait.until(EC.presence_of_element_located((By.ID, field_id)))
        field.clear()
        field.send_keys(value)

    def blur_field(self, field_id):
        """Quita el foco de un input para disparar validación HTML5"""
        field = self.driver.find_element(By.ID, field_id)
        self.driver.execute_script("arguments[0].blur();", field)
