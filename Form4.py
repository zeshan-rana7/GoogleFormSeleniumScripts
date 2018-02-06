import os
import time
from Utils import next_button_css,question_type_title_text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Form4(object):

    def __init__(self, driver):
        self.driver = driver

    def verify_page(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector(question_type_title_text).text

    def select_no_answer(self):
        self.driver.find_element_by_css_selector(next_button_css).click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")

    def click_first_dropdown(self):
        self.driver.find_element_by_css_selector(
            ".freebirdFormviewerViewItemsItemItem:nth-of-type(2) .quantumWizMenuPaperselectOptionList").click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector(
            ".exportSelectPopup.quantumWizMenuPaperselectPopup .exportOption")

    def click_second_dropdown(self):
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            ".freebirdFormviewerViewItemsItemItem:nth-of-type(3) .quantumWizMenuPaperselectOptionList").click()

    def select_one_answer(self):
        self.driver.find_element_by_css_selector(".exportSelectPopup.quantumWizMenuPaperselectPopup .exportOption[data-value='Lahore']").click()
        self.driver.find_element_by_css_selector(next_button_css).click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")

    def get_question_elements(self):
        return self.driver.find_elements_by_css_selector(".freebirdFormviewerViewItemsItemItemTitle.freebirdCustomFont")

    def select_first_answer_based_on_question(self, answer1):
        print answer1
        self.driver.find_element_by_css_selector(".exportSelectPopup.quantumWizMenuPaperselectPopup .exportOption[data-value='{value_dropbox}']".format(
            value_dropbox=answer1)).click()

    def select_second_answer_based_on_question(self, answer2):
        print answer2
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            ".exportSelectPopup.quantumWizMenuPaperselectPopup .exportOption[data-value='{value_dropbox}']".format(
                value_dropbox=answer2)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(next_button_css).click()
        # inputfield.send_keys(os.path.join(os.curdir, "registration_page.png"))


