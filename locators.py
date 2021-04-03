from selenium.webdriver.common.by import By

class Locators:
        titulo_home = 'My Store'
        buscar_produto = (By.ID,'search_query_top')
        pesquisar = (By.NAME,'submit_search')
        mensagem_retorno_pesquisa = (By.CLASS_NAME,'heading-counter')
        retornar_home = 'http://automationpractice.com/index.php'
        alerta_produto_inexistente = (By.XPATH, "//p[contains(@class,'alert alert-warning')]")
        alerta_esperado = 'No results were found for your search "produtoInexistente"'
        menu_woman = (By.CLASS_NAME,'sf-with-ul')
        banner_woman = (By.CLASS_NAME,'content_scene_cat_bg')
        produto_detalhes = (By.XPATH, "//a[@title='Blouse'][contains(.,'Blouse')]")
        pagina_produto = 'Blouse - My Store'
        add_to_cart = (By.XPATH, "//span[contains(.,'Add to cart')]")
        tag_blouse = (By.TAG_NAME,'h1')
        checkout = (By.XPATH,"//span[contains(.,'Proceed to checkout')]")
        advance_checkout = (By.CSS_SELECTOR, '.standard-checkout > span:nth-child(1)')
        login = (By.ID,"email_create")
        submmit = (By.ID,'SubmitCreate')