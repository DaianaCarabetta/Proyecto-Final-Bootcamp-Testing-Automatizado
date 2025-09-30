from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class HomePage:
    URL = "https://fake-cinema.vercel.app/"

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    CAROUSEL = (By.CSS_SELECTOR, "div[role='region'][aria-roledescription='carousel']")
    MOVIE_SLIDES = (By.CSS_SELECTOR, "div[role='group'][aria-roledescription='slide']")
    CAROUSEL_NEXT_BUTTON = (By.XPATH, "//button[.//span[text()='Next slide']]")
    CAROUSEL_PREV_BUTTON = (By.XPATH, "//button[.//span[text()='Previous slide']]")

    CARTELERA_SECTION = (By.CSS_SELECTOR, "section.container")
    MOVIE_TITLES = (By.CSS_SELECTOR, "section.container h3.font-bold")
    MOVIE_DETAIL_HEADER = (By.CSS_SELECTOR, "header h1.text-3xl.font-bold")

    def open(self):
        self.driver.get(self.URL)

    def is_carousel_loaded(self) -> bool:
        try:
            self.wait.until(EC.presence_of_element_located(self.CAROUSEL))
            slides = self.driver.find_elements(*self.MOVIE_SLIDES)
            return len(slides) > 0
        except TimeoutException:
            return False

    def click_carousel_next(self):
        carousel = self.wait.until(EC.presence_of_element_located(self.CAROUSEL))
        try:
            next_btn = carousel.find_element(
                By.XPATH, ".//button[contains(@class,'right-4') or .//span[contains(., 'Next slide')]]"
            )
        except NoSuchElementException:
            next_btn = carousel.find_element(By.XPATH, ".//button[not(contains(@class,'left-4')) and .//span]")
        self.wait.until(lambda d: next_btn.is_displayed() and next_btn.is_enabled())
        next_btn.click()

    def is_any_movie_visible_in_carousel(self) -> bool:
        try:
            slides = self.wait.until(EC.presence_of_all_elements_located(self.MOVIE_SLIDES))
            for slide in slides:
                try:
                    link = slide.find_element(By.TAG_NAME, "a")
                    href = link.get_attribute("href")
                    if "/movies/" in href:
                        return True
                except:
                    continue
            return False
        except TimeoutException:
            return False

    def is_cartelera_loaded(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.CARTELERA_SECTION))
            return True
        except TimeoutException:
            return False

    def has_movies_listed(self):
        try:
            self.wait.until(EC.presence_of_all_elements_located(self.MOVIE_TITLES))
            return True
        except TimeoutException:
            return False

    def scroll_to_cartelera(self):
        """Hace scroll hasta el título 'Cartelera'"""
        try:
            cartelera_header = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//h2[text()='Cartelera']"))
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior:'smooth', block:'start'});",
                cartelera_header
            )
        except TimeoutException:
            raise Exception("No se encontró la sección de cartelera")

    def select_movie(self, movie_name):
        """
        Selecciona la película por nombre en la grid de la cartelera
        y hace click en 'Ver detalle'.
        """
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.grid > div")))
        movie_card_xpath = f"//h3[normalize-space(text())='{movie_name}']/.."

        try:
            movie_card = self.wait.until(EC.visibility_of_element_located((By.XPATH, movie_card_xpath)))
            detail_link = movie_card.find_element(By.XPATH, ".//a[contains(text(),'Ver detalle')]")
            self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", detail_link)
            self.wait.until(EC.element_to_be_clickable(detail_link))
            detail_link.click()
        except TimeoutException:
            raise Exception(f"No se encontró la película '{movie_name}' en la cartelera")

    def is_movie_detail_loaded(self, movie_name: str):
        try:
            header = self.wait.until(EC.presence_of_element_located(self.MOVIE_DETAIL_HEADER))
            return movie_name.lower() in header.text.lower()
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def expected_movie_detail_url(self, movie_name: str):
        slug = movie_name.lower().replace(" ", "-")
        return f"https://fake-cinema.vercel.app/movies/{slug}"

