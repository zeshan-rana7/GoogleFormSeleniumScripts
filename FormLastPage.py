import os
import time
from Utils import next_button_css,question_type_title_text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class FormLastPage(object):

    def __init__(self, driver):
        self.driver = driver

    def verify_page(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector(".freebirdFormviewerViewResponseConfirmationMessage").text

    def click_view_score(self):
        window_before = self.driver.window_handles[0]
        print(window_before)
        self.driver.find_element_by_css_selector(".quantumWizButtonPaperbuttonLabel.exportLabel").click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.maximize_window()
        print(window_after)
