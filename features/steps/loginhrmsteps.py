from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.dashboardPages import DashboardPage
from pages.loginPages import LoginPage
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@given(u'Launch the browser')
def launchTheBrowser(context):
    context.driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager(driver_version="116.0.5845.96").install()))
    context.driver.maximize_window()
    context.loginPage = LoginPage(context.driver)
    context.dashboardPage = DashboardPage(context.driver)

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
        assert False, "Failed verify logo"

@then(u'Provide the username "{user}" and password "{pwd}"')
def enterLoginCreds(context,user, pwd):
    try:
        context.loginPage.enterLoginCredentials(user, pwd)
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

@then(u'Login is successful and dashboard is opened')
def validateDashboardPpage(context):
        try:
            context.dashboardPage.validatePageLoaded()
        except:
            context.driver.close()
            assert False, "Test is failed in validating dashboard"

@then(u'Provide the username "{user}"')
def enterLoginCreds(context, user):
    try:
        context.loginPage.inputUsername(user)
    except:
        context.driver.close()
        assert False, "Test is failed in enter password"

@then(u'Provide the passsword "{pwd}"')
def enterLoginCreds(context, pwd):
    try:
        context.loginPage.inputPassword(pwd)
    except:
        context.driver.close()
        assert False, "Test is failed in enter password"

@then(u'Login is failed with invalid credential')
def validateInvalidLogin(context):
    try:
        context.loginPage.validateInvalidCredential()
    except:
        context.driver.close()
        assert False, "Test is failed with invalid credentials"

@then(u'Login is failed and empty username error is displayed')
def validateEmptyUsername(context):
    try:
        context.loginPage.validateEmptyUsername()
    except:
        context.driver.close()
        assert False, "Test is failed in validate empty username"

@then(u'Login is failed and empty password error is displayed')
def validateEmptyPassword(context):
    try:
        context.loginPage.validateEmptyPassword()
    except:
        context.driver.close()
        assert False, "Test is failed in validate empty password"

@then(u'browser close')
def closeBrowser(context):
   context.driver.close()
