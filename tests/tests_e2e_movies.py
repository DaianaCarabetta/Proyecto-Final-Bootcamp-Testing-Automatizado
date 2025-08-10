import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
import pytest
from page_objects.base_page import BasePage

CONSTANTES_A USAR = "valor de la constante"

@pytest.mark.e2e
def test_user_movies_positive(driver):

    #ir al login
    #login -> llenar los campos

# class TestLogin:
#     @pytest.fixture(scope="class")
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("URL_DE_TU_APLICACION")
#         yield
#         self.driver.quit()
#
#     def test_login(self, setup):
#         login_page = LoginPage(self.driver)
#         login_page.login("usuario", "contraseña")
#         # Aquí puedes agregar aserciones para verificar el resultado
