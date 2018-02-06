import time


class Form1(object):

    def __init__(self, driver):
        self.driver = driver

    def fillForm1(self, cnic, phone, email, name):
        self.driver.find_element_by_css_selector("input[aria-label='CNIC']").send_keys(cnic)
        self.driver.find_element_by_css_selector("input[aria-label='Phone Number']").send_keys(phone)
        self.driver.find_element_by_css_selector("input[aria-label='Email']").send_keys(email)
        self.driver.find_element_by_css_selector("input[aria-label='Name']").send_keys(name)
        self.driver.find_element_by_css_selector(".freebirdFormviewerViewNavigationNoSubmitButton").click()
        time.sleep(2)
        return self.driver.find_elements_by_css_selector("div.freebirdFormviewerViewItemsItemErrorMessage")

    def clearformvalues(self):
        self.driver.find_element_by_css_selector("input[aria-label='CNIC']").clear()
        self.driver.find_element_by_css_selector("input[aria-label='Phone Number']").clear()
        self.driver.find_element_by_css_selector("input[aria-label='Email']").clear()
        self.driver.find_element_by_css_selector("input[aria-label='Name']").clear()


