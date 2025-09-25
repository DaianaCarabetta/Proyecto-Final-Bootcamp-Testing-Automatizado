from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_navegador():
    opts = Options()
    # opts.add_argument("--headless=new")  # descomenta si quieres sin UI
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    driver.set_window_size(1280, 800)
    return driver

base_url = "https://fake-cinema.vercel.app"
