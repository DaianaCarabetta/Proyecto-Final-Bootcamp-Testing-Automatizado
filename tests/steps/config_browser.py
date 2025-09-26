from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def iniciar_navegador(navegador="chrome"):
    if navegador == "firefox":
        opts = FirefoxOptions()
        # opts.add_argument("--headless")  # opcional
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)


    elif navegador == "edge":
        print("🧭 Iniciando Edge...")
        opts = EdgeOptions()
        # opts.add_argument("--headless")  # opcional
        driver = webdriver.Edge(service=EdgeService("C:\\WebDrivers\\Edge\\msedgedriver.exe"), options=opts)


    else:  # Chrome por defecto
        opts = ChromeOptions()
        # opts.add_argument("--headless=new")  # opcional
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

    driver.set_window_size(1280, 800)
    return driver

base_url = "https://fake-cinema.vercel.app"