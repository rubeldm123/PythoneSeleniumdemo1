import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Chrome(
        executable_path="C:/Users/rubel/Documents/pythonProject/demOrangeHRM/drivers/chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
