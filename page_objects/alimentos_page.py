from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

class AlimentosPage:
    class Locators:

        BASE_URL = 'https://fake-cinema.vercel.app/'

        ALIMENTOS_LINK = (By.LINK_TEXT, 'Alimentos')
        CART_LINK = (By.CSS_SELECTOR, "a[href='/cart']")
        ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Agregar al carrito']")

        PRODUCT_LINK_BY_NAME = "//h3[contains(normalize-space(),'{name}')]/ancestor::a"
        PRODUCT_IMG_BY_NAME = "//h3[normalize-space()='{name}']/ancestor::a//img"

        CART_PRODUCT_SPANS = (By.CSS_SELECTOR, "main div > div.flex.justify-between > span:first-child")

    def __init__(self, driver, timeout: int = 10, poll_frequency: float = 0.5):
        self.driver = driver
        self.timeout = timeout
        self.poll = poll_frequency
        self.wait = WebDriverWait(driver, timeout, poll_frequency=poll_frequency)
        self.actions = ActionChains(driver)
        self.hovered_element = None


    def _format_xpath(self, template: str, **kwargs):
        """Devuelve un locator (By.XPATH, xpath_formateado)."""
        return (By.XPATH, template.format(**kwargs))

    def _find(self, locator, timeout: int = None):
        t = timeout or self.timeout
        return WebDriverWait(self.driver, t, poll_frequency=self.poll).until(
            EC.presence_of_element_located(locator)
        )

    def _find_clickable(self, locator, timeout: int = None):
        t = timeout or self.timeout
        return WebDriverWait(self.driver, t, poll_frequency=self.poll).until(
            EC.element_to_be_clickable(locator)
        )

    def _click(self, locator, timeout: int = None):
        el = self._find_clickable(locator, timeout=timeout)
        el.click()
        return el

    def _find_all(self, locator, timeout: int = None):
        t = timeout or self.timeout
        WebDriverWait(self.driver, t, poll_frequency=self.poll).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def ir_a_seccion_alimentos(self):
        """Carga la página principal y hace click en 'Alimentos'."""
        self.driver.get(self.Locators.BASE_URL)
        self._click(self.Locators.ALIMENTOS_LINK)

    def ir_a_producto(self, nombre_producto: str):
        """Hace click en el link del producto por nombre (abre la página del producto)."""
        locator = self._format_xpath(self.Locators.PRODUCT_LINK_BY_NAME, name=nombre_producto)
        self._click(locator)

    def agregar_producto(self, cantidad: int = 1):
        """Click en 'Agregar al carrito' N veces (asume que estás en la página del producto)."""
        boton = self._find_clickable(self.Locators.ADD_BUTTON)
        for _ in range(cantidad):
            boton.click()

    def abrir_carrito(self):
        """Abre la vista del carrito."""
        self._click(self.Locators.CART_LINK)

    def obtener_cantidad_producto(self, nombre_producto: str, cantidad_esperada: int = None, max_wait: int = 10):
        """
        Devuelve la cantidad del producto en el carrito.
        Espera dinámicamente hasta encontrar el span que contiene 'Nombre x N'.
        Si cantidad_esperada se pasa, espera hasta que coincida.
        """
        self.abrir_carrito()

        start = time.time()
        while time.time() - start < max_wait:
            spans = self.driver.find_elements(*self.Locators.CART_PRODUCT_SPANS)
            for s in spans:
                text = s.text.strip()
                if text.startswith(nombre_producto):
                    try:
                        cantidad = int(text.split('x')[-1].strip())
                    except ValueError:
                        cantidad = 0
                    if cantidad_esperada is None or cantidad == cantidad_esperada:
                        return cantidad
            time.sleep(0.4)

        raise TimeoutException(f"No se encontró {nombre_producto} con cantidad {cantidad_esperada} en el carrito después de {max_wait}s.")

    # Hover / cursor
    def hover_producto(self, nombre_producto: str, timeout: int = None):
        """
        Hace hover sobre la imagen del producto (busca <img> dentro del <a> que contiene el <h3>).
        Guarda el elemento hovereado en self.hovered_element.
        """
        locator = self._format_xpath(self.Locators.PRODUCT_IMG_BY_NAME, name=nombre_producto)
        img = self._find(locator, timeout=timeout)
        self.actions.move_to_element(img).perform()
        self.hovered_element = img
        return img

    def obtener_cursor_hover(self):
        """Devuelve el valor CSS 'cursor' del último elemento hovereado."""
        if not self.hovered_element:
            return None
        return self.driver.execute_script("return window.getComputedStyle(arguments[0]).cursor;", self.hovered_element)

    def obtener_cursor_producto(self, nombre_producto: str, timeout: int = None):
        """
        Atajo: hace hover sobre el producto y devuelve el cursor actual (hover + read).
        Útil para assertions en steps sin mantener estado.
        """
        elem = self.hover_producto(nombre_producto, timeout=timeout)
        return self.driver.execute_script("return window.getComputedStyle(arguments[0]).cursor;", elem)

#caso limite
    def obtener_mensaje_error_limite(self):
        """
        Espera un mensaje de error visible relacionado con el límite máximo de unidades.
        Retorna el texto del mensaje si aparece, o None si no se muestra.
        """
        try:
            mensaje = self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//*[contains(text(), 'límite') or contains(text(), 'máximo') or contains(text(), 'no puedes agregar')]"
                ))
            )
            return mensaje.text
        except TimeoutException:
            return None
