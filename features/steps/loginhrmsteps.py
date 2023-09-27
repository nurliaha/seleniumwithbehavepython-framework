from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.loginPages import LoginPage
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@given(u'Launch the browser')
def launchtheBrowser(context):
    context.driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager(driver_version="116.0.5845.96").install()))
    context.driver.maximize_window()
    context.loginPage = LoginPage(context.driver)


@then(u'Open the https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
def openLink(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)


@when(u'Verify that the logo present')
def verifyLogoHRM(context):
    try:
        location = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]")
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(location))
        return element.is_displayed()
    except:
        context.driver.close()
        assert False, "Failed vrify logo"


@then(u'Input valid username "{user}" and password "{pwd}"')
def enter_login_creds(context,user, pwd):
    try:
        context.loginPage.enter_login_credentials(user, pwd)
    except:
        context.driver.close()
        assert False, "Test is failed in enter login credentials"


@then(u'Click login button')
def clickLoginButton (context):
    try:
        context.loginPage.clickBtnLogin()
        time.sleep(5)
    except:
        context.driver.close()
        assert False, "Test is failed in enter login"



# @then(u'Login is successful and dashboard is opened')
# def dashboardHRM(context):
#     raise NotImplementedError(u'STEP: Then Login is successful and dashboard is opened')

#
# @then(u'browser close')
# def browserClose(context):
#     raise NotImplementedError(u'STEP: Then browser close')
