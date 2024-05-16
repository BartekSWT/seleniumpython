from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.edit_project_page import EditProjectPage



class AddProjectPage:
    new_project_name = (By.CSS_SELECTOR, '#name')
    new_project_prefix = (By.CSS_SELECTOR, '#prefix')
    new_project_description = (By.CSS_SELECTOR, '#description')
    save_button = (By.CSS_SELECTOR, '[value=Zapisz')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def create_new_project(self, name, prefix, description):
        self.wait.until(lambda x: self.browser.find_element(*self.new_project_name))
        self.browser.find_element(*self.new_project_name).send_keys(name)
        self.wait.until(lambda x: self.browser.find_element(*self.new_project_prefix))
        self.browser.find_element(*self.new_project_prefix).send_keys(prefix)
        self.wait.until(lambda x: self.browser.find_element(*self.new_project_description))
        self.browser.find_element(*self.new_project_description).send_keys(description)
        self.wait.until(EC.element_to_be_clickable(self.save_button))
        self.browser.find_element(*self.save_button).click()
        return EditProjectPage(self.browser)
