from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # ---------- SELECTORES ----------
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

    # ---------- MÉTODOS ----------
    def is_loaded(self):
        """Verifica que estemos en Checkout"""
        return self.wait.until(EC.presence_of_element_located(self.TITLE))

    def is_item_displayed(self, nombre_producto, precio):
        """Verifica que un producto con precio aparezca en el resumen"""
        productos = self.driver.find_elements(*self.PRODUCT_LIST)
        for producto in productos:
            spans = producto.find_elements(By.TAG_NAME, "span")
            if spans and nombre_producto in spans[0].text and precio in spans[1].text:
                return True
        return False

    def get_total(self):
        """Obtiene el total de la compra"""
        return self.driver.find_element(*self.TOTAL).text

    def fill_form(self, nombre, apellido, email, card_name, card_number, cvv):
        """Completa el formulario con los datos dados"""
        self.driver.find_element(*self.INPUT_FIRSTNAME).send_keys(nombre)
        self.driver.find_element(*self.INPUT_LASTNAME).send_keys(apellido)
        self.driver.find_element(*self.INPUT_EMAIL).send_keys(email)
        self.driver.find_element(*self.INPUT_CARDNAME).send_keys(card_name)
        self.driver.find_element(*self.INPUT_CARDNUMBER).send_keys(card_number)
        self.driver.find_element(*self.INPUT_CVV).send_keys(cvv)

    def confirm_payment(self):
        """Hace clic en Confirmar pago"""
        boton = self.driver.find_element(*self.CONFIRM_BUTTON)
        boton.click()

    def get_success_message(self):
        """Devuelve el mensaje de compra exitosa"""
        try:
            return self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE)).text
        except:
            return None

    def get_field_validation_message(self, field_id):
        """Devuelve el mensaje de validación de un input HTML5"""
        field = self.driver.find_element(By.ID, field_id)
        return self.driver.execute_script(
            "return arguments[0].validationMessage;", field
        )

    def is_confirm_button_enabled(self):
        """Verifica si el botón de confirmar está habilitado"""
        return self.driver.find_element(*self.CONFIRM_BUTTON).is_enabled()

    def fill_field(self, field_id, value):
        """Completa un input específico con el valor dado"""
        field = self.driver.find_element(By.ID, field_id)
        field.clear()
        field.send_keys(value)

    def blur_field(self, field_id):
        """Quita el foco de un input para disparar validación HTML5"""
        field = self.driver.find_element(By.ID, field_id)
        self.driver.execute_script("arguments[0].blur();", field)
