from selenium.webdriver.common.by import By

from pageObjects.PurchasePage import Purchase


class Confirm:
    def __init__(self, driver):
        self.driver = driver

    purchase=(By.XPATH,"//button[@class='btn btn-success']")

    def confirm(self):
        self.driver.find_element(*Confirm.purchase).click()
        country = Purchase(self.driver)
        return country



