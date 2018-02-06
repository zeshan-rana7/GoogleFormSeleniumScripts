from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class LoginPage(object):

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def visit(self):
        self.driver.get(self.url)
        # If login button is visible on form page instead of popup uncomment this line
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".freebirdFormviewerViewMelbaGLogo"))
        # )
        # If login popup visible
        WebDriverWait(self.driver, 10).until(
             EC.visibility_of_element_located((By.CSS_SELECTOR, ".quantumWizDialogPaperdialogBottomButtons .quantumWizButtonPaperbuttonEl:nth-of-type(2)"))
         )

    def Login(self, Email, Passwrod):
        #self.driver.find_element_by_css_selector(".freebirdFormviewerViewMelbaSignInButton").click()
        self.driver.find_element_by_css_selector(".quantumWizDialogPaperdialogBottomButtons .quantumWizButtonPaperbuttonEl:nth-of-type(2)").click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#identifierNext"))
        )
        email_elem = self.driver.find_element_by_css_selector("#identifierId")
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#next")))
        # email_elem = self.driver.find_element_by_css_selector("#Email")
        email_elem.send_keys(Email)
        email_elem.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".whsOnd.zHQkBf[type='password']")))
        password_elem = self.driver.find_element_by_css_selector(".whsOnd.zHQkBf[type='password']")
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, "#Passwd")))
        # password_elem = self.driver.find_element_by_css_selector("#Passwd")
        password_elem.send_keys(Passwrod)
        password_elem.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            ".freebirdFormviewerViewHeaderTitle.freebirdCustomFont"))
        )


