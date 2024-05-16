from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.projects_page import ProjectsPage


class EditProjectPage:
    projects_icon = (By.CSS_SELECTOR, 'a[href="http://demo.testarena.pl/administration/projects"]')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def click_projects_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.projects_icon))
        self.browser.find_element(*self.projects_icon).click()
        return ProjectsPage(self.browser)
