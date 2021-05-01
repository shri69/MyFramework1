import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from Utilities.BaseClass import BaseClass

from pageObjects.CheckoutPage import CheckOut
from pageObjects.ConfirmPage import Confirm
from pageObjects.HomePage import HomePage
from pageObjects.PurchasePage import Purchase


@pytest.mark.usefixtures("setup")
class Test_one(BaseClass):
    def test_e2e(self):
        log=self.getLogger()
        homePage = HomePage(self.driver)
        homePage.gotoShop()

        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")

        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                checkout = CheckOut(self.driver)
                checkout.addTocart().click()
                checkout.Checkout().click()

        #confirm page
        buy = Confirm(self.driver)
        country=buy.confirm()
        #logging.info("country selection")

        #purchase page
        #country = Purchase(self.driver)
        country.Send().send_keys("ind")

        #wait = WebDriverWait(self.driver, 7)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verify("India")
        country.Select().click()

        country.Check().click()

        country.Submit().click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText
        log.info("successfully submited")


        self.driver.get_screenshot_as_file("screen.png")

