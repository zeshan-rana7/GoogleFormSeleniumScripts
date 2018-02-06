import os
import time
from Utils import next_button_css,question_type_title_text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Form6(object):

    def __init__(self, driver):
        self.driver = driver

    def verify_page(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector(question_type_title_text).text

    def select_no_answer(self):
        self.driver.find_element_by_css_selector(next_button_css).click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")

    def get_question_elements(self):
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemItemTitle.freebirdCustomFont")

    def select_answer_based_on_question(self, answer1):
        self.driver.find_element_by_css_selector(".quantumWizTogglePaperradioEl[data-value ='{radio_box}']".format(
            radio_box=answer1)).click()
        self.driver.find_element_by_css_selector(next_button_css).click()