from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProjectsPage:
    no_project_div = (By.CSS_SELECTOR, '.empty-text')
    search_project_input = (By.CSS_SELECTOR, '#search')
    search_project_icon = (By.CSS_SELECTOR, '#j_searchButton')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def search_project(self, name):
        self.wait.until(lambda x: self.browser.find_element(*self.search_project_input))
        self.browser.find_element(*self.search_project_input).send_keys(name)
        self.wait.until(EC.element_to_be_clickable(self.search_project_icon))
        self.browser.find_element(*self.search_project_icon).click()
        self.wait.until(lambda x: self.browser.find_element(By.LINK_TEXT, name))
        return self.browser.find_element(By.LINK_TEXT, name)
