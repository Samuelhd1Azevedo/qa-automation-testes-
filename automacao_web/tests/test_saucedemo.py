import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from automacao_web.pages.sauce_pages import SaucePages

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_deve_realizar_compra_com_sucesso(driver):
    page = SaucePages(driver)
    page.realizar_login("standard_user", "secret_sauce")
    page.adicionar_produto_ao_carrinho()
    page.ir_para_checkout()
    page.preencher_dados_checkout("John", "Doe", "12345")
    page.finalizar_compra()
    
    mensagem_esperada = "Thank you for your order!"
    assert page.obter_mensagem_sucesso() == mensagem_esperada
