from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver, timeout: int=10):
        self.driver = driver
        self.timeout = timeout

        # ---------- Locators positivos ----------
        self.item_locator = "//h3[text()='{name}']"
        self.add_to_cart_button = "//button[contains(., 'Agregar al carrito')]"
        self.back_to_alimentos_link = "//a[contains(., 'Alimentos')]"
        self.cart_link = "//a[contains(., 'Carrito')]"
        self.checkout_button = "//a[@href='/checkout']//button"
        self.subtotal_locator = "//div[.//span[normalize-space()='Subtotal']]/span[2]"
        self.total_locator = "//div[.//span[normalize-space()='Total']]/span[2]"
        self.cart_header = "//h1[normalize-space()='Carrito']"

        # ---------- Locators negativos (no existen en la app, se prueban como BUGs) ----------
        self.cart_items = "//div[contains(@class,'flex') and .//span]"
        self.remove_button = "//button[contains(., 'Eliminar')]"
        self.increase_button = "//button[contains(., '+')]"
        self.decrease_button = "//button[contains(., '-')]"


    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.XPATH, locator))
        )

    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

    def select_item(self, item_name):
        self.wait_for_clickable(self.item_locator.format(name=item_name)).click()

    def add_to_cart(self):
        self.wait_for_clickable(self.add_to_cart_button).click()

    def go_back_to_alimentos(self):
        self.wait_for_clickable(self.back_to_alimentos_link).click()

    def go_to_cart(self):
        self.wait_for_clickable(self.cart_link).click()

    def click_checkout(self):
        """Hace clic en el botón de checkout y espera la redirección"""
        self.wait_for_clickable(self.checkout_button).click()
        WebDriverWait(self.driver, self.timeout).until(
            EC.url_contains("/checkout")
        )

    def is_item_displayed(self, item_name, price):
        row_locator = f"//div[contains(@class,'flex') and .//span[contains(normalize-space(.), '{item_name}')]]"
        try:
            row = self.wait_for_visible(row_locator)
            price_elem = row.find_element(By.XPATH, ".//span[2]")
            return price_elem.text.strip() == price
        except:
            return False

    def get_subtotal(self):
        return self.wait_for_visible(self.subtotal_locator).text.strip()

    def get_total(self):
        return self.wait_for_visible(self.total_locator).text.strip()

    def is_cart_loaded(self):
        """Valida que la vista de Carrito esté cargada correctamente"""
        try:
            self.wait_for_visible(self.cart_header)
            return True
        except:
            return False

    # ---------- Validaciones negativas ----------
    def has_items(self):
        """Verifica si hay productos en el carrito"""
        return len(self.driver.find_elements(By.XPATH, self.cart_items)) > 0

    def has_remove_button(self):
        """Devuelve True si existe un botón de eliminar"""
        return len(self.driver.find_elements(By.XPATH, self.remove_button)) > 0

    def has_increase_button(self):
        """Devuelve True si existe un botón de incrementar cantidad"""
        return len(self.driver.find_elements(By.XPATH, self.increase_button)) > 0

    def has_decrease_button(self):
        """Devuelve True si existe un botón de disminuir cantidad"""
        return len(self.driver.find_elements(By.XPATH, self.decrease_button)) > 0
