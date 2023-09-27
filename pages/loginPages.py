from pages.basePages import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    TXT_USERNAME = (By.NAME, "username")
    TXT_PASSWORD = (By.NAME, "password")
    BTN_LOGIN = (By.XPATH, "//button[text()=' Login ']")
    MSG_INVALIDCREDS = (By.ID, "spanMessage")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self, user, pwd):
        self.input_element(self.TXT_USERNAME, user)
        self.input_element(self.TXT_PASSWORD, pwd)

    def inputUsername(self, username):
        self.input_element(self.TXT_USERNAME, username)


    def inputPassword (self, password):
        self.input_element(self.TXT_PASSWORD, password)

    def clickBtnLogin(self):
        self.click_element(self.BTN_LOGIN)

    def setLoginusername(self, username):
        self.inputUsername(username)

    def setLoginPassword(self, pwd):
        self.inputPassword(pwd)

