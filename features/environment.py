# features/environment.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    context.base_url = "https://fake-cinema.vercel.app"

def before_scenario(context, scenario):
    opts = Options()
    # opts.add_argument("--headless=new")  # descomenta si quieres sin UI
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                      options=opts)
    context.driver.set_window_size(1280, 800)

def after_scenario(context, scenario):
    context.driver.quit()
