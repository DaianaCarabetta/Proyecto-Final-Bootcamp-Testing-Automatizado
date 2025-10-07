from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

class DetailPage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    MOVIE_TITLE = (By.CSS_SELECTOR, "header h1.text-3xl.font-bold")
    MOVIE_BANNER = (By.CSS_SELECTOR, "header img[alt^='Banner de']")
    MOVIE_POSTER = (By.CSS_SELECTOR, "header img[alt^='Poster de']")
    MOVIE_GENRES = (By.CSS_SELECTOR, "header div.flex.items-center.gap-4 span:first-child")
    MOVIE_DURATION = (By.XPATH, "//header//span[contains(text(),'min')]")
    SHOWTIME_DAYS = (By.CSS_SELECTOR, "main div.flex.items-center button")
    LANGUAGE_SECTION_XPATH = "//h3[normalize-space(text())='{language}']/following-sibling::div"

    def is_loaded(self) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(self.MOVIE_TITLE))
            return True
        except TimeoutException:
            return False

    def get_title(self) -> str:
        return self.wait.until(EC.presence_of_element_located(self.MOVIE_TITLE)).text

    def select_second_day(self):
        """Selecciona el segundo botón de día (mañana)"""
        days = self.wait.until(EC.presence_of_all_elements_located(self.SHOWTIME_DAYS))
        if len(days) < 2:
            raise Exception("No hay suficientes días de funciones disponibles")

        days[1].click()
        self.selected_day_index = 1

        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                f"(//main//div[contains(@class,'flex')]/button)[2]//div[contains(@class,'text-2xl')]"
            ))
        )

    def get_selected_day_text(self):
        index = getattr(self, "selected_day_index", 0)
        number_div = self.wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                f"(//main//div[contains(@class,'flex')]/button)[{index + 1}]//div[contains(@class,'text-2xl')]"
            ))
        )
        number = number_div.text.strip()
        span_elements = self.driver.find_elements(
            By.XPATH,
            f"(//main//div[contains(@class,'flex')]/button)[{index + 1}]/span"
        )
        month = span_elements[1].text.strip() if len(span_elements) > 1 else ""
        return f"{number} de {month}"

    def get_languages(self):
        langs = self.driver.find_elements(By.CSS_SELECTOR, "main h3.text-lg.font-semibold")
        return [lang.text.strip() for lang in langs]

    def get_showtimes(self, language: str):
        try:
            section = self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.LANGUAGE_SECTION_XPATH.format(language=language)))
            )
            buttons = section.find_elements(By.TAG_NAME, "button")
            return [btn.text.split("\n")[0] for btn in buttons]
        except TimeoutException:
            return []

    def select_showtime(self, language: str, time: str):
        section = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.LANGUAGE_SECTION_XPATH.format(language=language)))
        )
        button = section.find_element(By.XPATH, f".//button[contains(., '{time}')]")
        button.click()

    def select_first_showtime_in_language(self, language: str):
        section = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.LANGUAGE_SECTION_XPATH.format(language=language)))
        )
        buttons = section.find_elements(By.TAG_NAME, "button")
        valid_buttons = []
        now = datetime.now().time()

        for btn in buttons:
            try:
                text = btn.text.split("\n")[0].strip()
                showtime = datetime.strptime(text, "%I:%M %p").time()
                if showtime > now:
                    valid_buttons.append(btn)
            except ValueError:
                continue

        if not valid_buttons:
            raise Exception(f"No hay horarios futuros en {language} disponibles")
        valid_buttons[0].click()

    def is_book_page_loaded(self, movie_name: str) -> bool:
        """Valida que la página de book se haya cargado correctamente"""
        slug = movie_name.lower().replace(" ", "-")
        expected_url = f"/movies/{slug}/book"
        try:
            self.wait.until(lambda d: expected_url in d.current_url)
            cart_title = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.w-full h3.font-bold"))
            ).text
            return cart_title == movie_name
        except TimeoutException:
            return False

