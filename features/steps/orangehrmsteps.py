
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@given(u'launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version="116.0.5845.96").install()))
    context.driver.maximize_window()


@when(u'open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)


@then(u'verify that the logo present on page')
def verivyLogo(context):
    status = context.driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
