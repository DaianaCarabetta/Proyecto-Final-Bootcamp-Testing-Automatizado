from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PromosPage:
    URL = "https://fake-cinema.vercel.app/promos"

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    COMBO_PAREJA_CARD = (By.XPATH, "//h3[normalize-space()='Combo Pareja']/../..")
    COMBO_PAREJA_HEADER = (By.XPATH, "//h1[normalize-space()='Combo Pareja']")
    AGREGAR_AL_CARRITO_BUTTON = (By.XPATH, "//button[contains(text(),'Agregar al carrito')]")

    def open(self):
        self.driver.get(self.URL)

    def is_combo_pareja_available(self):
        try:
            card = self.wait.until(EC.presence_of_element_located(self.COMBO_PAREJA_CARD))
            return card.is_displayed()
        except TimeoutException:
            return False

    def select_combo_pareja(self):
        card = self.wait.until(EC.element_to_be_clickable(self.COMBO_PAREJA_CARD))
        card.click()

    def is_combo_pareja_page_loaded(self):
        try:
            header = self.wait.until(EC.presence_of_element_located(self.COMBO_PAREJA_HEADER))
            return header.is_displayed()
        except TimeoutException:
            return False

    def click_agregar_al_carrito(self):
        button = self.wait.until(EC.element_to_be_clickable(self.AGREGAR_AL_CARRITO_BUTTON))
        button.click()

    def is_seat_selection_page_loaded(self):
        """Valida si la página de selección de asientos se cargó"""
        try:
            self.wait.until(lambda d: "/book" in d.current_url)
            return True
        except TimeoutException:
            return False

    def is_payment_page_loaded(self):
        """Valida si la página de pago se cargó"""
        try:
            self.wait.until(lambda d: "/cart" in d.current_url)
            return True
        except TimeoutException:
            return False

