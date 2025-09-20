from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5

        self.item_locator = "//span[contains(text(), '{name}')]"
        self.price_locator = "//span[contains(text(), '{price}')]"
        self.subtotal_locator = "//span[contains(text(), 'Subtotal')]/following-sibling::span"
        self.total_locator = "//span[contains(text(), 'Total')]/following-sibling::span"
        self.checkout_button = "//button[contains(., 'Proceder al pago')]"

        # Controles (que la app NO tiene → usados en negativos)
        self.remove_button = "//button[contains(., 'Eliminar')]"
        self.increase_button = "//button[contains(., '+')]"
        self.decrease_button = "//button[contains(., '-')]"
        self.cart_items = "//div[contains(@class,'flex') and .//span]"

    # ---------- Métodos positivos ----------
    def is_item_displayed(self, item_name, price):
        try:
            row_locator = f"//div[contains(@class,'flex') and .//span[contains(text(),'{item_name}')]]"
            row = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.XPATH, row_locator))
            )
            return price in row.text
        except:
            return False

    def get_subtotal(self):
        subtotal = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, self.subtotal_locator))
        )
        return subtotal.text.strip()

    def get_total(self):
        total = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, self.total_locator))
        )
        return total.text.strip()

    def click_checkout(self):
        boton = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button))
        )
        boton.click()

    # ---------- Métodos negativos ----------
    def has_items(self):
        """Verifica si hay productos en el carrito"""
        items = self.driver.find_elements(By.XPATH, self.cart_items)
        return len(items) > 0

    def has_remove_button(self):
        """Devuelve True si existe un botón de eliminar"""
        return len(self.driver.find_elements(By.XPATH, self.remove_button)) > 0

    def has_increase_button(self):
        """Devuelve True si existe el botón de incrementar cantidad"""
        return len(self.driver.find_elements(By.XPATH, self.increase_button)) > 0

    def has_decrease_button(self):
        """Devuelve True si existe el botón de disminuir cantidad"""
        return len(self.driver.find_elements(By.XPATH, self.decrease_button)) > 0
