from selenium.webdriver.common.by import By

#from BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOut


class HomePage():

    def __init__(self,driver):
        self.driver=driver
    shop=(By.CSS_SELECTOR,"a[href*='shop']")
    name=(By.CSS_SELECTOR,"input[name='name']")
    email=(By.NAME,"email")
    checkBox=(By.ID,"exampleCheck1")
    gender=(By.ID,"exampleFormControlSelect1")
    password=(By.ID,"exampleInputPassword1")
    submit=(By.XPATH,"//input[@type='submit']")
    message=(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible")

    def gotoShop(self):
         self.driver.find_element(*HomePage.shop).click()
         checkoutpage=CheckOut(self.driver)
         return checkoutpage

    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
         return self.driver.find_element(*HomePage.email)

    def getCheck(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccess(self):
        return self.driver.find_element(*HomePage.message)

