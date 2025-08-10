#herramientas Driver, utils para generar datos aleatorios,
#traer datos de algun lado, leer un archivo csv, etc
#metodos auxiliares

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver


def create_driver(headless: bool = False):
    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--windows-size=1920, 1080")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )

    driver.implicity_wait(5)
    return driver