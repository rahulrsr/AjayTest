#import pageObject.NewsLetter as N_L
from pageObject.NewsLetter import NewsLetter
from selenium import webdriver
import time

class test():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def test_run(self):
        driver = self.driver
        url = "http://automationpractice.com/index.php?"
        driver.get(url)
        obj=NewsLetter(driver)
        #obj.letter_input_field_fun.send_keys("rahul@gmail.com")
        obj.letter_input_field_fun().send_keys("rahul@gmail.com")
        obj.submit_btn_fun().click()
        time.sleep(5)
        assert obj.alert_box_fun().text=="Newsletter : This email address is already registered2."



if __name__ == '__main__':
    t=test()
    t.test_run()


