from selenium.webdriver.common.by import By

class SignIn:
    def __init__(self,driver):
        self.driver=driver

    CreateAccountButton=(By.XPATH,"//button[@id='SubmitCreate']")
    New_Email_Address_Field=(By.XPATH,"//input[@name='email_create']")
    Login_Email_Address_Field=(By.XPATH,"//input[@id='email']")
    Login_Password_Field = (By.XPATH, "// input[ @ id = 'passwd']")
    SingIn_button=(By.XPATH,"//button[@id='SubmitLogin']")
    Create_Account_Message=(By.XPATH,"//ol/li")


    def get_CreateAccountButton(self):
        return self.driver.find_element(*SignIn.CreateAccountButton)

    def get_New_Email_Input_Field(self):
        return self.driver.find_element(*SignIn.New_Email_Address_Field)

    def get_login_Email_Input_Field(self):
        return self.driver.find_element(*SignIn.Login_Email_Address_Field)

    def get_login_Password_Input_Field(self):
        return self.driver.find_element(*SignIn.Login_Password_Field)

    def get_Sign_In_Button(self):
        return self.driver.find_element(*SignIn.SingIn_button)

    def get_account_creation_message(self):
        return self.driver.find_element(*SignIn.Create_Account_Message)