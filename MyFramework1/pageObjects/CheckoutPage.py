from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import Confirm


class CheckOut:
    def __init__(self,driver):
        self.driver=driver

    addtocart=(By.XPATH,"//div[@class='card h-100']/div[2]/button")
    cart=(By.XPATH,"//a[@class='nav-link btn btn-primary']")

    def addTocart(self):
        return self.driver.find_element(*CheckOut.addtocart)

    def Checkout(self):
        return self.driver.find_element(*CheckOut.cart)

