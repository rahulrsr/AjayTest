from selenium import webdriver
import time

url="http://automationpractice.com/index.php?"

driver=webdriver.Chrome()
driver.get(url)

"""
describe('This test case describes about user subscription to newsletter', function() {  
    it('user should be able to subscribe himself for newsletter', async function (done) {
      await AutomationPracticeHome_Page.scrollToViewHeading();
      await AutomationPracticeHome_Page.enterEmailNewsLetter("chrishemsworthyz@you-spam.com");
      await AutomationPracticeHome_Page.submitNewsLetterButton();
      await browser.pause(3000);
      await AutomationPracticeHome_Page.isSuccessAlertExists();
      await AutomationPracticeHome_Page.confirmSuccessfulNewsLetterSubscription();
    });



  async enterEmailNewsLetter(emailAddress){
    return await ((await this.newsletterInputField).setValue(emailAddress));
  }
get newsletterInputField() {
    return $("//input[@id='newsletter-input']");
  }  
  
   async submitNewsLetterButton(){
    return await (await this.submitNewsletter).click();
  } 
get submitNewsletter(){
    return $("//button[@name='submitNewsletter']");
  }
async confirmSuccessfulNewsLetterSubscription(){ 
  var successfulSubscriptionHeader = "//p[@class='alert alert-success']";
  var validateSuccessfulSubscriptionHeader = await browser.waitUntil(async function () {
    return (await(await $(successfulSubscriptionHeader)).getText() == "Newsletter : You have successfully subscribed to this newsletter.")
  }, 3000);
  assert.equal(validateSuccessfulSubscriptionHeader, true);
}

async confirmUnSuccessfulNewsLetterSubscription(){
  var unsuccessfulSubs


async confirmUnSuccessfulNewsLetterSubscription(){
  var unsuccessfulSubscriptionHeader = "//p[@class='alert alert-danger']";
    var validateUnsuccessfulSubscriptionHeader = await browser.waitUntil(async function () {
      return (await(await $(unsuccessfulSubscriptionHeader)).getText() =="Newsletter : This email address is already registered.");
    }, 3000);
    assert.equal(validateUnsuccessfulSubscriptionHeader, true);
 }
"""

#driver.find_element_by_id('newsletter-input')
driver.find_element_by_xpath("//input[@id='newsletter-input']").send_keys("rahul@gmail.com")
driver.find_element_by_xpath("//button[@name='submitNewsletter']").click()
time.sleep(5)
alert_box=driver.find_element_by_xpath("//p[@class='alert alert-danger']")

assert alert_box.text=="Newsletter : This email address is already registered."


