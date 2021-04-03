from abc import ABC
from locators import Locators
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from faker import Faker
from test_ecommerce import Locators


class TestEcommerce(Locators):
    def test_home_page(self, produto):
        assert self.titulo_home in webdriver.title
        webdriver.find_element(*self.buscar_produto).send_keys(produto)
        webdriver.find_element(*self.pesquisar).click()

    def test_search_page(self):
        # assert self.titulo in webdriver.title
        wait = WebDriverWait(webdriver, 10).until(
            EC.presence_of_element_located(self.mensagem_retorno_pesquisa)
        )

    def test_search_not_found(self, produto_nao_existente):
        webdriver.get(self.retornar_home)
        assert self.titulo_home in webdriver.title
        webdriver.find_element(*self.buscar_produto).send_keys(produto_nao_existente)
        webdriver.find_element(*self.pesquisar).click()
        msg = webdriver.find_element(*self.alerta_produto_inexistente).text
        assert self.alerta_esperado in msg

    def test_category_page(self):
        element_to_hover_over = webdriver.find_element(*self.menu_woman)
        hover = ActionChains(webdriver).move_to_element(element_to_hover_over)
        hover.perform()
        webdriver.find_element(*self.menu_woman).click()
        sleep(2)
        title_categ = webdriver.title
        assert "Women - My Store" in title_categ

        wait = WebDriverWait(webdriver, 10).until(
            EC.presence_of_element_located(self.banner_woman)
        )

    def test_product_page(self):
        webdriver.find_element(*self.produto_detalhes).click()
        assert self.pagina_produto in webdriver.title
        product = webdriver.find_element(*self.tag_blouse).text
        assert "Blouse" in product

    def test_add_to_card(self):
        webdriver.find_element(*self.add_to_cart).click()
        sleep(2)
        # wait = WebDriverWait(webdriver, 10).until(
        #    EC.presence_of_element_located('layer_cart_product_title')
        # )
        webdriver.find_element(*self.checkout).click()

    def test_confirmation(self):
        page_confirmation = webdriver.title
        assert "Order - My Store" in page_confirmation
        sleep(1)
        webdriver.find_element(*self.advance_checkout).click()

    def test_login_page(self):
        faker = Faker()
        login_title = webdriver.title
        assert "Login - My Store" in login_title
        webdriver.find_element(*self.login).send_keys(faker.email())
        webdriver.find_element(*self.submmit).click()
        autenticar = webdriver.find_element_by_class_name("navigation_page").text
        assert "Authentication" in autenticar
        print(faker.email())

    def test_cadastro(self):

        sleep(10)

    def close_webdriver(self):
        webdriver.quit()


url = "http://automationpractice.com"

webdriver = Firefox()
ecommerce = TestEcommerce(webdriver, url)

ecommerce.open()
ecommerce.test_home_page("Blouse")
ecommerce.test_search_not_found("produtoInexistente")
ecommerce.test_search_page()
ecommerce.test_category_page()
ecommerce.test_product_page()
ecommerce.test_add_to_card()
ecommerce.test_confirmation()
ecommerce.test_login_page()
ecommerce.close_webdriver()
