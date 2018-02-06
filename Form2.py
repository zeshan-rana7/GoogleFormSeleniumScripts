import time
from Utils import next_button_css,question_type_title_text


class Form2(object):

    def __init__(self, driver):
        self.driver = driver

    def verify_page(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector(question_type_title_text).text

    def select_answer(self, case):
        if case == 0:
            self.driver.find_element_by_css_selector(next_button_css).click()
            time.sleep(2)
            return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")
        elif case == 1:
            self.driver.find_element_by_css_selector(".exportLabelWrapper>[data-value='Password']").click()
            self.driver.find_element_by_css_selector(next_button_css).click()
            time.sleep(2)
            return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")

    def get_questions_answers_block(self):
        return self.driver.find_elements_by_css_selector(".freebirdFormviewerViewItemsItemItem")

    def get_question_text(self,block_elem):
        return block_elem.find_element_by_css_selector("div.freebirdFormviewerViewItemsItemItemTitle.freebirdCustomFont").text

    def get_answers_text(self, block_elem):
        return block_elem.find_elements_by_css_selector(".freebirdFormviewerViewItemsRadioLabel")

    def select_answer_based_on_question(self, answer1, answer2):
        self.driver.find_element_by_css_selector(".exportLabelWrapper>[data-value='{radio_box}']".format(
            radio_box=answer1)).click()
        self.driver.find_element_by_css_selector(".exportLabelWrapper>[data-value='{radio_box}']".format(
            radio_box=answer2)).click()
        self.driver.find_element_by_css_selector(next_button_css).click()
