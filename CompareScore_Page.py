import os
import time
from Utils import next_button_css,question_type_title_text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CompareScorePage(object):

    def __init__(self, driver):
        self.driver = driver

    def verify_page(self):
        time.sleep(5)
        return self.driver.find_element_by_css_selector(".freebirdFormviewerViewHeaderGradeContainer").text

    def get_user_total_score(self):
        return self.driver.find_element_by_css_selector(".freebirdFormviewerViewHeaderGradeFraction.freebirdSolidBackground").text

    def get_user_each_attempted_question_score(self):
        return self.driver.find_elements_by_css_selector(
            ".freebirdFormviewerViewItemsItemScore")