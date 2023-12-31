import time

from pages.basePages import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):
    TXT_DASHBOARD = (By.XPATH, "// h6[text() = 'Dashboard']")
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

    # Board menu:
    TITLE_TIME = (By.XPATH, "//h6[text()='Time']")
    def __init__(self, driver):
        super().__init__(driver)

    def validatePageLoaded(self):
        self.verify_element_displayed(self.TXT_DASHBOARD)
        assert self.get_element_text(self.TXT_DASHBOARD) == "Dashboard"

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

    def inputSearch(self, search):
        self.verify_element_displayed(self.SEARCH)
        self.input_element(self.SEARCH, search)

    def validateSearchTime(self):
        self.verify_element_displayed(self.MENU_TIME)
        time.sleep(3)
        assert self.get_element_text(self.MENU_TIME) == "Time"

    def validaBoardTime(self):
        self.verify_element_displayed(self.TITLE_TIME)
        assert self.get_element_text(self.TITLE_TIME) == "Time"






