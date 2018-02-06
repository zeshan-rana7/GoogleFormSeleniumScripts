import os
import time
from Utils import next_button_css,question_type_title_text
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Form5(object):

    def __init__(self, driver):
        self.driver = driver

    def verify_page(self):
        time.sleep(2)
        return self.driver.find_element_by_css_selector(question_type_title_text).text

    def select_no_answer(self):
        self.driver.find_element_by_css_selector(next_button_css).click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")

    def upload_one_file(self):
        self.driver.find_element_by_css_selector(".freebirdFormviewerViewItemsItemItem:nth-of-type(2) .quantumWizButtonPaperbuttonLabel.exportLabel").click()
        time.sleep(2)
        iframe = self.driver.find_element_by_css_selector(".picker.modal-dialog.picker-dialog:nth-last-child(2) .picker-frame")
        self.driver.switch_to_frame(iframe)
        time.sleep(5)
        self.driver.find_element_by_css_selector(".a-Xh:nth-of-type(2) ").click()
        time.sleep(10)
        self.driver.find_element_by_css_selector(".Vi-Ll-to-Kc.Vi-rj-sj:nth-of-type(1) .pj-Ll-to.pj-Ll-Vk.pj-Ll-Ik-rj-sj.pj-Tm-Ek").click()
        time.sleep(5)
        self.driver.find_element_by_css_selector("div[id='picker:ap:2']").click()
        self.driver.switch_to_default_content()
        self.driver.find_element_by_css_selector(next_button_css).click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")
        # time.sleep(3)
        # button = self.driver.find_element_by_css_selector("button")
        # valbutton = button.get_attribute("style")
        # print button
        # print valbutton
        # inputfield= self.driver.find_element_by_css_selector("input[type='file']")
        # val = inputfield.get_attribute("style")
        # print inputfield
        # print val
        # self.driver.execute_script('arguments[0].style.display = "block";',button)
        # self.driver.execute_script('arguments[0].style.visibility = "visible";',inputfield)
        # valbutton = button.get_attribute("style")
        # val = inputfield.get_attribute("style")
        # print val
        # print valbutton
        # time.sleep(10)

    def upload_first_file(self):
        self.driver.find_element_by_css_selector(".freebirdFormviewerViewItemsItemItem:nth-of-type(2) .quantumWizButtonPaperbuttonLabel.exportLabel").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".picker.modal-dialog.picker-dialog:nth-last-child(2) .picker-frame"))
        )
        iframe = self.driver.find_element_by_css_selector(".picker.modal-dialog.picker-dialog:nth-last-child(2) .picker-frame")
        self.driver.switch_to_frame(iframe)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".a-Xh:nth-of-type(2) "))
        )
        self.driver.find_element_by_css_selector(".a-Xh:nth-of-type(2) ").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".Vi-Ll-to-Kc.Vi-rj-sj:nth-of-type(1) .pj-Ll-to.pj-Ll-Vk.pj-Ll-Ik-rj-sj.pj-Tm-Ek"))
        )
        self.driver.find_element_by_css_selector(".Vi-Ll-to-Kc.Vi-rj-sj:nth-of-type(1) .pj-Ll-to.pj-Ll-Vk.pj-Ll-Ik-rj-sj.pj-Tm-Ek").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "div[id='picker:ap:2']"))
        )
        self.driver.find_element_by_css_selector("div[id='picker:ap:2']").click()
        self.driver.switch_to_default_content()

    def upload_second_file(self):
        self.driver.find_element_by_css_selector(".freebirdFormviewerViewItemsItemItem:nth-of-type(3) .quantumWizButtonPaperbuttonLabel.exportLabel").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".picker.modal-dialog.picker-dialog:nth-last-child(2) .picker-frame"))
        )
        iframe = self.driver.find_element_by_css_selector(".picker.modal-dialog.picker-dialog:nth-last-child(2) .picker-frame")
        self.driver.switch_to_frame(iframe)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".a-Xh:nth-of-type(2) "))
        )
        self.driver.find_element_by_css_selector(".a-Xh:nth-of-type(2) ").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              ".Vi-Ll-to-Kc.Vi-rj-sj:nth-of-type(1) .pj-Ll-to.pj-Ll-Vk.pj-Ll-Ik-rj-sj.pj-Tm-Ek"))
        )
        self.driver.find_element_by_css_selector(".Vi-Ll-to-Kc.Vi-rj-sj:nth-of-type(1) .pj-Ll-to.pj-Ll-Vk.pj-Ll-Ik-rj-sj.pj-Tm-Ek").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "div[id='picker:ap:2']"))
        )
        self.driver.find_element_by_css_selector("div[id='picker:ap:2']").click()
        self.driver.switch_to_default_content()
        self.driver.find_element_by_css_selector(next_button_css).click()