from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Account_Creation:
    def __init__(self,driver):
        self.driver=driver

    Radio_Button_Mr = (By.XPATH,"//div[@class='radio'][@id='uniform-id_gender1']")
    Radio_Button_Mrs = (By.XPATH,"//div[@class='radio'][@id='uniform-id_gender2']")
    FirstName=(By.ID,"customer_firstname")
    LastName=(By.ID,"customer_lastname")
    Email_address=(By.ID,"email")
    Password=(By.ID,"passwd")
    Day=(By.ID,"days") #select
    Month = (By.ID, "months") #select
    years=(By.ID,"years") #select
    Address_FirstName=(By.ID,"firstname")
    Address_LastName =(By.ID,"lastname")
    Address_Line1=(By.ID,"address1")
    Address_City=(By.ID,"city")
    Address_State = (By.ID, "id_state")
    Address_post_code=(By.ID,"postcode")
    Address_Mobile=(By.ID,"phone_mobile")
    Address_alias=(By.ID,"alias")
    Register_Button=(By.ID,"submitAccount")

    def Radio_Button_Mr_fun(self):
        return self.driver.find_element(*Account_Creation.Radio_Button_Mr)

    def Radio_Button_Mrs_fun(self):
        return self.driver.find_element(*Account_Creation.Radio_Button_Mrs)

    def FirstName_fun(self):
        return self.driver.find_element(*Account_Creation.FirstName)

    def LastName_fun(self):
        return self.driver.find_element(*Account_Creation.LastName)

    def Email_address_fun(self):
        return self.driver.find_element(*Account_Creation.Email_address)

    def Password_fun(self):
        return self.driver.find_element(*Account_Creation.Password)

    def Day_dd_fun(self):
        return Select(self.driver.find_element(*Account_Creation.Day))

    def Month_dd_fun(self):
        return Select(self.driver.find_element(*Account_Creation.Month))

    def years_dd_fun(self):
        return Select(self.driver.find_element(*Account_Creation.Month))

    def Address_FirstName_fun(self):
        return self.driver.find_element(*Account_Creation.Address_FirstName)

    def Address_LastName_fun(self):
        return self.driver.find_element(*Account_Creation.Address_LastName)

    def Address_Line1_fun(self):
        return self.driver.find_element(*Account_Creation.Address_LastName)


    def Address_City_fun(self):
        return self.driver.find_element(*Account_Creation.Address_City)


    def Address_State_dd_fun(self):
        return Select(self.driver.find_element(*Account_Creation.Address_State))

    def Address_Post_Code_fun(self):
        return self.driver.find_element(*Account_Creation.Address_post_code)


    def Address_Mobile_fun(self):
        return self.driver.find_element(*Account_Creation.Address_Mobile)

    def Address_alias_fun(self):
        return self.driver.find_element(*Account_Creation.Address_alias)

    def Register_Button_fun(self):
        return self.driver.find_element(*Account_Creation.Register_Button)



