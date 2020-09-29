import allure
import pytest
from pages.HomPage import homePage
from pages.LoginPage import loginPage
from utils import utils as utils
import moment
from selenium import webdriver


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_tc1login(self):
        driver = self.driver
        driver.get(utils.url)
        lp = loginPage(driver)
        lp.entersername(utils.username)
        lp.enterusersassword(utils.password)
        lp.clickonloginbtn()

    def test_tc2logout(self):
        try:
            driver = self.driver
            hp = homePage(driver)
            hp.clickOnWelcomeLink()
            hp.clickOnLogOutBtn()
            x = driver.title
            assert x == "abc"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            #currenTime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testName=utils.callfuction()
            screenShotName=testName+"_"+utils.cueeentTime()
            allure.attach(self.driver.get_screenshot_as_png(), name=screenShotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/rubel/Documents/pythonProject/demo1/screenshots" + screenShotName + ".png")
            raise
        except:
            print("There was an exception")
            raise
