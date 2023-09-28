from pages.basePages import BasePage
from selenium.webdriver.common.by import By

class MenuPage(BasePage):
    SEARCH = (By.CSS_SELECTOR, "[placeholder='Search']")
    MENU_ADMIN = (By.XPATH, "//span[text()='Admin']")
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    MENU_LEAVE = (By.XPATH, "//span[text()='Leave']")
    MENU_TIME = (By.XPATH, "//span[text()='Time']")
    MENU_RECRUITMENT = (By.XPATH, "//span[text()='Recruitment']")
    MENU_MYINFO = (By.XPATH, "//span[text()='My Info']")
    MENU_PERFORMANCE = (By.XPATH, "//span[text()='Performance']")
    MENU_DASHBOARD = (By.XPATH, "//span[text()='Dashboard']")
    MENU_DIRECTORY = (By.XPATH, "//span[text()='Directory']")
    MENU_MAINTANANCE = (By.XPATH, "//span[text()='Maintenance']")
    MENU_CLAIM = (By.XPATH, "//span[text()='Claim']")
    MENU_BUZZ = (By.XPATH, "//span[text()='Buzz']")

    def __init__(self, driver):
        super().__init__(driver)

    def clickBtnSearch(self):
        self.verify_element_displayed(self.SEARCH)
        self.click_element(self.SEARCH)

    def clickBtnAdmin(self):
        self.verify_element_displayed(self.MENU_ADMIN)
        self.click_element(self.MENU_ADMIN)

    def clickBtnPim(self):
        self.verify_element_displayed(self.MENU_PIM)
        self.click_element(self.MENU_PIM)

    def clickBtnLeave(self):
        self.verify_element_displayed(self.MENU_LEAVE)
        self.click_element(self.MENU_LEAVE)

    def clickBtnTime(self):
        self.verify_element_displayed(self.MENU_TIME)
        self.click_element(self.MENU_TIME)

    def clickBtnRecruitment(self):
        self.verify_element_displayed(self.MENU_RECRUITMENT)
        self.click_element(self.MENU_RECRUITMENT)

    def clickBtnMyInfo(self):
        self.verify_element_displayed(self.MENU_MYINFO)
        self.click_element(self.MENU_MYINFO)

    def clickBtnPerformance(self):
        self.verify_element_displayed(self.MENU_PERFORMANCE)
        self.click_element(self.MENU_PERFORMANCE)

    def clickBtnDashboard(self):
        self.verify_element_displayed(self.MENU_DASHBOARD)
        self.click_element(self.MENU_DASHBOARD)

    def clickBtnClaim(self):
        self.verify_element_displayed(self.MENU_CLAIM)
        self.click_element(self.MENU_CLAIM)

    def clickBtnBuzz(self):
        self.verify_element_displayed(self.MENU_BUZZ)
        self.click_element(self.MENU_BUZZ)