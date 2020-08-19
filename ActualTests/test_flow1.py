import pytest
from pageObject.NewsLetter import NewsLetter
from pageObject.HomePage import homepage
from pageObject.SignInPage import SignIn
from pageObject.CreateAccount import Account_Creation
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestFirst:
    def test_NewsLetter_already_registered(self):
        # driver = self.driver
        # url = "http://automationpractice.com/index.php?"
        # driver.get(url)
        obj=NewsLetter(self.driver)
        #obj.letter_input_field_fun.send_keys("rahul@gmail.com")
        obj.letter_input_field_fun().send_keys("rahul@gmail.com")
        obj.submit_btn_fun().click()
        #time.sleep(5)
        #driver.implicitly_wait(5)
        assert obj.alert_box_existing_msg_fun().text=="Newsletter : This email address is already registered."

    def test_NewsLetter_successfully_subscribed(self):
        # driver = self.driver
        # url = "http://automationpractice.com/index.php?"
        # driver.get(url)
        obj=NewsLetter(self.driver)
        #obj.letter_input_field_fun.send_keys("rahul@gmail.com")
        obj.letter_input_field_fun().send_keys("rahul12q34kq5q11we@gmail.com")
        obj.submit_btn_fun().click()
        #time.sleep(5)
        #driver.implicitly_wait(5)
        print(self.driver.title)
        assert obj.alert_box_success_msg_fun().text=="Newsletter : You have successfully subscribed to this newsletter."

    def test_signIn_New(self):
        home=homepage(self.driver)
        home.get_SignIn_Button().click()
        signInPage=SignIn(self.driver)
        signInPage.get_New_Email_Input_Field().send_keys("abc1267as@gmail.com")
        #assert signInPage.CreateAccountButton()
        signInPage.get_CreateAccountButton().click()
        print(self.driver.title)
        #//form/div[@class='account_creation'][1]/h3[@class='page-subheading']
        WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.XPATH,"//form/div[@class='account_creation'][1]/h3[@class='page-subheading']"))
        )
        #alert_text=signInPage.get_account_creation_message().text
        #assert alert_text==""

    def test_create_account(self):
        CreateAccount=Account_Creation(self.driver)
        CreateAccount.Radio_Button_Mr_fun().click()
        CreateAccount.FirstName_fun().send_keys("TestR")
        CreateAccount.LastName_fun().send_keys("TestLast")
        CreateAccount.Email_address_fun().send_keys("testr@testmail.com")
        CreateAccount.Password_fun().send_keys("Test@123")
        CreateAccount.Day_dd_fun().select_by_visible_text('2')
        CreateAccount.Month_dd_fun().select_by_value(2)
        CreateAccount.years_dd_fun().select_by_value(1976)
        CreateAccount.Address_FirstName_fun().send_keys("TestR")
        CreateAccount.Address_LastName_fun().send_keys("TestLast")
        CreateAccount.Address_Line1_fun().send_keys("TestAddress")
        CreateAccount.Address_City_fun().send_keys("Juneau")
        CreateAccount.Address_State_dd_fun().select_by_value('Alaska')
        CreateAccount.Address_Post_Code_fun().send_keys('99501')
        CreateAccount.Address_Mobile_fun().send_keys('9014568727')
        CreateAccount.Address_alias_fun().send_keys('testAlaska')
        CreateAccount.Register_Button_fun().click()


