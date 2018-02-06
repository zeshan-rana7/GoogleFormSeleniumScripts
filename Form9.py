import os
import time
from Utils import next_button_css,question_type_title_text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Form9(object):

    def __init__(self, driver):
        self.driver = driver

    def verify_page(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector(question_type_title_text).text

    def select_no_answer(self):
        self.driver.find_element_by_css_selector(next_button_css).click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")

    def select_one_answer(self):
        self.driver.find_element_by_css_selector(".freebirdFormviewerViewItemsGridRowGroup:nth-of-type(2) .freebirdFormviewerViewItemsGridCheckbox[data-value='Reading']").click()
        self.driver.find_element_by_css_selector(next_button_css).click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")

    def get_question_elements(self):
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemItemTitle.freebirdCustomFont")

    def input_date_time(self, month, day, year, hour, minute, am_pm):
        print am_pm
        self.driver.find_element_by_css_selector("input[aria-label='Month']").send_keys(month)
        self.driver.find_element_by_css_selector("input[aria-label='Day of the month']").send_keys(day)
        self.driver.find_element_by_css_selector("input[aria-label='Year']").send_keys(year)
        self.driver.find_element_by_css_selector("input[aria-label='Hour']").send_keys(hour)
        self.driver.find_element_by_css_selector("input[aria-label='Minute']").send_keys(minute)
        self.driver.find_element_by_css_selector(".quantumWizMenuPaperselectDropDown.exportDropDown").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(".exportSelectPopup.quantumWizMenuPaperselectPopup .exportOption[data-value='{value_ampm}']".format(value_ampm=am_pm)).click()
        #self.driver.find_element_by_css_selector(".exportSelectPopup.quantumWizMenuPaperselectPopup .exportOption[data-value='PM']").click()
        self.driver.find_element_by_css_selector(next_button_css).click()

