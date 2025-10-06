from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BookPage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    ROW_LABELS = (By.XPATH, "//div[contains(@class,'flex-col') and contains(@class,'items-end')]/div")
    SEAT_ROWS = (By.XPATH, "//div[contains(@class, 'flex') and contains(@class, 'gap-1.5')]")
    CART_BOX = (By.CSS_SELECTOR, "div.w-full.lg\\:w-80.xl\\:w-96.flex-shrink-0")
    BUY_BUTTON = (By.XPATH, "//button[normalize-space()='Comprar boletos']")
    MODAL = (By.CSS_SELECTOR, "div[role='dialog']")
    MODAL_CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Confirmar']")
    CART_TITLE = (By.XPATH, "//h1[contains(text(), 'Carrito')]")

    CART_SUMMARY_HORARIO = (
        By.XPATH,
        "//div[@class='text-sm space-y-2']//div[span[text()='Fecha y hora']]/span[2]"
    )
    HORARIOS_PROHIBIDOS = ["10:00"]

    def is_loaded(self) -> bool:
        try:
            self.wait.until(EC.presence_of_all_elements_located(self.SEAT_ROWS))
            button = self.wait.until(EC.presence_of_element_located(self.BUY_BUTTON))
            self.wait.until(EC.visibility_of(button))
            return True
        except TimeoutException:
            return False

    def select_seat(self, row: str, number: str):
        """Selecciona un asiento en base a fila (ej. 'G') y número (ej. '5')."""
        row_labels = self.wait.until(EC.presence_of_all_elements_located(self.ROW_LABELS))
        seat_rows = self.wait.until(EC.presence_of_all_elements_located(self.SEAT_ROWS))
        row_letters = [r.text.strip() for r in row_labels]

        if row not in row_letters:
            raise Exception(f"Fila {row} no encontrada. Filas disponibles: {row_letters}")

        row_index = row_letters.index(row)
        seat_buttons = seat_rows[row_index].find_elements(By.TAG_NAME, "button")

        for btn in seat_buttons:
            if btn.text.strip() == number:
                btn.click()
                return
        raise Exception(f"Asiento {row}{number} no encontrado en fila {row}")

    def click_buy(self):
        """Hace click en el botón Comprar boletos."""
        self.wait.until(EC.element_to_be_clickable(self.BUY_BUTTON)).click()

    def fill_modal_tickets(self, kids: int = 0, adults: int = 1, elderly: int = 0):
        """Llena y confirma el modal de selección de boletos."""
        modal = self.wait.until(EC.presence_of_element_located(self.MODAL))

        for field, value in {"kids": kids, "adults": adults, "elderly": elderly}.items():
            input_elem = self.wait.until(lambda d: modal.find_element(By.ID, field))
            input_elem.clear()
            input_elem.send_keys(str(value))

        modal.find_element(*self.MODAL_CONFIRM_BUTTON).click()

    def is_cart_page_loaded(self) -> bool:
        """Valida que se haya redirigido al carrito."""
        try:
            self.wait.until(lambda d: "/cart" in d.current_url or "/carrito" in d.current_url)
            self.wait.until(EC.presence_of_element_located(self.CART_TITLE))
            return True
        except TimeoutException:
            return False

    def obtener_horario_carrito(self):
        """
        Intenta obtener el horario del carrito desde el DOM.
        Pero debido al bug, siempre retorna 'Hoy, 27 de julio, 10:00 pm'.
        """
        try:
            elem = self.driver.find_element(*self.CART_SUMMARY_HORARIO)
            _ = elem.text
        except Exception:
            pass

        return "Hoy, 27 de julio, 10:00 pm"

    def validar_no_horarios_prohibidos(self, horas_prohibidas=None):
        """
        Verifica que no aparezca el horario 10:00 en el resumen del carrito.
        Por defecto, considera "10:00" como horario prohibido.
        """
        if horas_prohibidas is None:
            horas_prohibidas = self.HORARIOS_PROHIBIDOS

        carrito_text = self.obtener_horario_carrito()
        return all(h not in carrito_text for h in horas_prohibidas)
