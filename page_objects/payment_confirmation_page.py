from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    TITLE = (By.XPATH, "//h1[contains(text(), 'Pago completado')]")
    ORDER_NUMBER = (By.XPATH, "//p[contains(text(), 'Compra #')]")
    SUMMARY_SECTION = (By.CSS_SELECTOR, "main div.mt-4")
    TOTAL = (By.XPATH, "//div[contains(@class,'font-bold')]/span[last()]")
    RETURN_HOME_BUTTON = (By.XPATH, "//button[contains(., 'Volver al inicio')]")


    def is_loaded(self):
        """Verifica que la página de confirmación se haya cargado"""
        try:
            self.wait.until(EC.presence_of_element_located(self.TITLE))
            return True
        except:
            return False

    def is_purchase_summary_displayed(self):
        """Valida que se muestre el resumen de la compra"""
        return self.driver.find_element(*self.SUMMARY_SECTION).is_displayed()

    def get_total_amount(self):
        """Obtiene el monto total de la compra"""
        return self.driver.find_element(*self.TOTAL).text

    def get_order_number(self):
        """Obtiene el número de orden de la compra"""
        return self.wait.until(EC.presence_of_element_located(self.ORDER_NUMBER)).text

    def click_return_home(self):
        """Hace clic en el botón 'Volver al inicio'"""
        boton = self.wait.until(EC.element_to_be_clickable(self.RETURN_HOME_BUTTON))
        boton.click()
