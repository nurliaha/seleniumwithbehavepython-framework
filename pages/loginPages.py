from pages.basePages import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    TXT_USERNAME = (By.NAME, "username")
    TXT_PASSWORD = (By.NAME, "password")
    BTN_LOGIN = (By.XPATH, "//button[text()=' Login ']")
    MSG_ERR = (By.XPATH, "//span[text()='Required']")
    MSG_INVALIDCREDS = (By.XPATH, "//p[text()='Invalid credentials']")

    def __init__(self, driver):
        super().__init__(driver)

    def enterLoginCredentials(self, user, pwd):
        self.input_element(self.TXT_USERNAME, user)
        self.input_element(self.TXT_PASSWORD, pwd)

    def inputUsername(self, username):
        self.verify_element_displayed(self.TXT_USERNAME)
        self.input_element(self.TXT_USERNAME, username)

    def inputPassword (self, password):
        self.verify_element_displayed(self.TXT_PASSWORD)
        self.input_element(self.TXT_PASSWORD, password)

    def clickBtnLogin(self):
        self.verify_element_displayed(self.BTN_LOGIN)
        self.click_element(self.BTN_LOGIN)

    def validateEmptyUsername(self):
        self.verify_element_displayed(self.MSG_ERR)
        assert self.get_element_text(self.MSG_ERR) == "Required"

    def validateEmptyPassword(self):
        self.verify_element_displayed(self.MSG_ERR)
        assert self.get_element_text(self.MSG_ERR) == "Required"

    def validateInvalidCredential(self):
        self.verify_element_displayed(self.MSG_INVALIDCREDS)
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "Invalid credentials"

