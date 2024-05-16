import random
import string

from fixtures.chrome import chrome_browser
from fixtures.testarena.login import browser
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.messages_page import MessagesPage

administrator_email = 'administrator@testarena.pl'


def test_successful_login(browser):
    home_page = HomePage(browser)
    user_email = home_page.get_current_user_email()
    assert administrator_email == user_email


def test_add_message(browser):
    my_text = generate_random_string(10)

    home_page = HomePage(browser)
    home_page.click_mail_icon()

    messages_page = MessagesPage(browser)
    messages_page.add_message(my_text)
    messages_page.verify_message_added(my_text)

def test_add_new_project(browser):
    project_prefix = generate_random_string(5)
    project_name = "Bartek" + project_prefix
    project_description = "This is Bartek's project"

    home_page = HomePage(browser)
    admin_page = home_page.click_admin_icon()
    add_project_page = admin_page.click_add_project()
    edit_project_page = add_project_page.create_new_project(project_name, project_prefix, project_description)
    projects_page = edit_project_page.click_projects_icon()
    assert projects_page.search_project(project_name)


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
