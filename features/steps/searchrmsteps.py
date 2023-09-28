from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.dashboardPages import DashboardPage
from pages.loginPages import LoginPage
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

@given(u'Open the link orange hrm')
def launchTheBrowser(context):
    context.driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager(driver_version="116.0.5845.96").install()))
    context.driver.maximize_window()
    context.loginPage = LoginPage(context.driver)
    context.dashboardPage = DashboardPage(context.driver)
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)


@then(u'input the username "{user}" and password "{pwd}"')
def enterLoginCreds(context,user, pwd):
    try:
        context.loginPage.enterLoginCredentials(user, pwd)
    except:
        context.driver.close()
        assert False, "Test is failed in enter login credentials"

@then(u'input menu "{time}"')
def inputMenuTime(context, time):
    try:
        context.dashboardPage.inputSearch(time)
    except:
        context.driver.close()
        assert False, "Test is failed in enter search"

@then(u'menu time is displayed')
def validateSectionMenu(context):
    try:
        context.dashboardPage.validateSearchTime()
    except:
        context.driver.close()
        assert False, "Test is failed in displayed the section menu"
