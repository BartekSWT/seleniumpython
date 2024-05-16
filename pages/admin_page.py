from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.add_project_page import AddProjectPage


class AdminPage:
    add_project = (By.CSS_SELECTOR, 'a[href="http://demo.testarena.pl/administration/add_project"')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def click_add_project(self):
        self.wait.until(EC.element_to_be_clickable(self.add_project))
        self.browser.find_element(*self.add_project).click()
        return AddProjectPage(self.browser)
