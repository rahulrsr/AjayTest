from selenium.webdriver.common.by import By

class homepage:
    def __init__(self,driver):
        self.driver=driver

    SignInButton=(By.XPATH,"//a[@class='login']")

    def get_SignIn_Button(self):
        return self.driver.find_element(*homepage.SignInButton)