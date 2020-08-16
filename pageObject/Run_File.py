#import pageObject.NewsLetter as N_L
from pageObject.NewsLetter import NewsLetter
from selenium import webdriver
#from selenium.webdriver impor
import time

class test():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)


    def test_run(self):
        driver = self.driver
        url = "http://automationpractice.com/index.php?"
        driver.get(url)
        obj=NewsLetter(driver)
        #obj.letter_input_field_fun.send_keys("rahul@gmail.com")
        obj.letter_input_field_fun().send_keys("rahul@gmail.com")
        obj.submit_btn_fun().click()
        #time.sleep(5)
        #driver.implicitly_wait(5)
        assert obj.alert_box_existing_msg_fun().text=="Newsletter : This email address is already registered."

    def test_success_message(self):
        driver = self.driver
        url = "http://automationpractice.com/index.php?"
        driver.get(url)
        obj=NewsLetter(driver)
        #obj.letter_input_field_fun.send_keys("rahul@gmail.com")
        obj.letter_input_field_fun().send_keys("rahul12@gmail.com")
        obj.submit_btn_fun().click()
        #time.sleep(5)
        #driver.implicitly_wait(5)
        assert obj.alert_box_success_msg_fun().text=="Newsletter : You have successfully subscribed to this newsletter."



if __name__ == '__main__':
    t=test()
    t.test_run()
    t.test_success_message()


