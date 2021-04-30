import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        fileHandler = logging.FileHandler('logfile.log')
        logger.addHandler(fileHandler)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        return logger

    def verify(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def selectOption(self,locator,index):
        dropdown = Select(locator)
        dropdown.select_by_index(index)
