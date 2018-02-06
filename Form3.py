import time
from Utils import next_button_css,question_type_title_text

class Form3(object):

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
        self.driver.find_element_by_css_selector(".exportLabelWrapper>[aria-label='21']").click()
        self.driver.find_element_by_css_selector(next_button_css).click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")

    def get_question_elements(self):
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemItemTitle.freebirdCustomFont")

    def select_answer_based_on_question(self, answer1, answer2, answer3, answer4):
        self.driver.find_element_by_css_selector(".exportLabelWrapper>[aria-label='{radio_box}']".format(
            radio_box=answer1)).click()
        self.driver.find_element_by_css_selector(".exportLabelWrapper>[aria-label='{radio_box}']".format(
            radio_box=answer2)).click()
        self.driver.find_element_by_css_selector(".exportLabelWrapper>[aria-label='{radio_box}']".format(
            radio_box=answer3)).click()
        self.driver.find_element_by_css_selector(".exportLabelWrapper>[aria-label='{radio_box}']".format(
            radio_box=answer4)).click()
        self.driver.find_element_by_css_selector(next_button_css).click()
