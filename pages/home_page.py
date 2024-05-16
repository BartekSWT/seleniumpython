from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.admin_page import AdminPage
from pages.messages_page import MessagesPage


class HomePage:
    user_email = (By.CSS_SELECTOR, ".user-info small")
    mail_icon = (By.CLASS_NAME, 'icon_mail')
    admin_icon = (By.CSS_SELECTOR, 'a[href="http://demo.testarena.pl/administration"]')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def get_current_user_email(self):
        return self.browser.find_element(*self.user_email).text

    def click_mail_icon(self):
        self.browser.find_element(*self.mail_icon).click()
        return MessagesPage(self.browser)

    def click_admin_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.admin_icon))
        self.browser.find_element(*self.admin_icon).click()
        return AdminPage(self.browser)
