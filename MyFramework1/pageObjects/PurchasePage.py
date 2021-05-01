from selenium.webdriver.common.by import By


class Purchase:
    def __init__(self,driver):
        self.driver=driver

    send_country=(By.ID,"country")
    select_country=(By.LINK_TEXT,"India")
    check_box=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    submit=(By.CSS_SELECTOR,"[type='submit']")

    def Send(self):
        return self.driver.find_element(*Purchase.send_country)

    def Select(self):
        return self.driver.find_element(*Purchase.select_country)

    def Check(self):
        return self.driver.find_element(*Purchase.check_box)

    def Submit(self):
        return self.driver.find_element(*Purchase.submit)