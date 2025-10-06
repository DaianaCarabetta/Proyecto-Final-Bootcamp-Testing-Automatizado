from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import sys
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def _create_driver():
    """Crea el driver según el navegador definido en la variable BROWSER."""
    browser = os.getenv("BROWSER", "chrome").lower()
    print(f">>> Iniciando pruebas en navegador: {browser}")

    try:
        if browser == "chrome":
            opts = ChromeOptions()
            # opts.add_argument("--headless=new")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)

        elif browser == "firefox":
            opts = FirefoxOptions()
            # opts.add_argument("--headless")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)

        elif browser == "edge":
            opts = EdgeOptions()
            # opts.add_argument("--headless")
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=opts
            )
        else:
            raise ValueError(f"Navegador no soportado: {browser}")

        return driver
    except Exception as e:
        print(f"[!] Error al crear el driver para {browser}: {e}")
        print("[!] Intentá verificar conexión a Internet o driver local.")
        raise


def before_all(context):
    print(">>> before_all ejecutado")
    context.base_url = "https://fake-cinema.vercel.app"
    os.makedirs("screenshots", exist_ok=True)


def before_feature(context, feature):
    """Modo persistente solo si el feature tiene tag @e2e"""
    if "e2e" in feature.tags:
        print(f">>> before_feature ejecutado para {feature.name} [E2E MODE]")
        context.reuse_driver = True
        context.driver = _create_driver()
        context.driver.set_window_size(1280, 800)

        from page_objects.home_page import HomePage
        from page_objects.detail_page import DetailPage
        from page_objects.book_page import BookPage
        from page_objects.cart_page import CartPage
        from page_objects.checkout_page import CheckoutPage
        from page_objects.payment_confirmation_page import ConfirmationPage

        context.home_page = HomePage(context.driver)
        context.detail_page = DetailPage(context.driver)
        context.book_page = BookPage(context.driver)
        context.cart_page = CartPage(context.driver)
        context.checkout_page = CheckoutPage(context.driver)
        context.payment_confirmation_page = ConfirmationPage(context.driver)
    else:
        context.reuse_driver = False


def before_scenario(context, scenario):
    print(f">>> before_scenario ejecutado para: {scenario.name}")
    if not getattr(context, "reuse_driver", False):
        context.driver = _create_driver()
        context.driver.set_window_size(1280, 800)


def after_scenario(context, scenario):
    print(f">>> after_scenario ejecutado para: {scenario.name}")

    # Intentar tomar screenshot solo si el driver existe y sigue vivo
    if hasattr(context, "driver") and context.driver:
        if scenario.status == "failed":
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"screenshots/{scenario.name.replace(' ', '_')}_{timestamp}.png"
            try:
                context.driver.save_screenshot(screenshot_path)
                print(f"[!] Captura guardada en: {screenshot_path}")
            except Exception as e:
                print(f"⚠️ No se pudo tomar screenshot: {e}")

    # Cerrar driver solo si no estamos reusándolo y sigue activo
    try:
        if not getattr(context, "reuse_driver", False):
            if hasattr(context, "driver") and context.driver:
                context.driver.quit()
    except Exception as e:
        print(f"⚠️ Error cerrando driver: {e}")




def after_feature(context, feature):
    if getattr(context, "reuse_driver", False):
        print(f">>> after_feature ejecutado para {feature.name} [E2E MODE]")
        try:
            if hasattr(context, "driver") and context.driver:
                context.driver.quit()
        except WebDriverException:
            print("⚠️ Driver ya estaba cerrado")


def after_all(context):
    print(">>> after_all ejecutado - Todas las pruebas finalizadas")
