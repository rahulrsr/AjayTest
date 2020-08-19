from selenium import webdriver
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver=webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.get("http://automationpractice.com/index.php?")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    #driver.close()