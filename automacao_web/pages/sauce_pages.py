from selenium.webdriver.common.by import By

class SaucePages:
    def __init__(self, driver):
        self.driver = driver
        
        # Mapeamento de elementos (Locators)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.add_bike_light_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    # Ações da página
    def realizar_login(self, user, passw):
        self.driver.find_element(*self.username_input).send_keys(user)
        self.driver.find_element(*self.password_input).send_keys(passw)
        self.driver.find_element(*self.login_button).click()

    def adicionar_produto_ao_carrinho(self):
        self.driver.find_element(*self.add_bike_light_button).click()
        self.driver.find_element(*self.shopping_cart).click()

    def ir_para_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def preencher_dados_checkout(self, first, last, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first)
        self.driver.find_element(*self.last_name_input).send_keys(last)
        self.driver.find_element(*self.postal_code_input).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def finalizar_compra(self):
        self.driver.find_element(*self.finish_button).click()

    def obter_mensagem_sucesso(self):
        return self.driver.find_element(*self.complete_header).text