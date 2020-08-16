from selenium.webdriver.common.by import By

class NewsLetter:
    letter_input_field=(By.XPATH,"//input[@id='newsletter-input']")
    submit_btn=(By.XPATH,"//button[@name='submitNewsletter']")
    alert_box_existing_msg = (By.XPATH, "//p[@class='alert alert-danger']")
    alert_box_success_msg = (By.XPATH, "//p[@class='alert alert-success']")
    def __init__(self,driver):
        self.driver=driver

    def letter_input_field_fun(self):
        return self.driver.find_element(*NewsLetter.letter_input_field)

    def submit_btn_fun(self):
        return self.driver.find_element(*NewsLetter.submit_btn)

    def alert_box_existing_msg_fun(self):
        return self.driver.find_element(*NewsLetter.alert_box_existing_msg)
    def alert_box_success_msg_fun(self):
        return self.driver.find_element(*NewsLetter.alert_box_success_msg)