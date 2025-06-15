import time
import pytest
from selenium.webdriver.common.by import By
from pages.contact_page import ContactPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_contact_page(driver):
    contact_page = ContactPage(driver)
    contact_page.open_page()
    time.sleep(1)
    contact_page.click_element(contact_page.contact_locator)

    assert contact_page.get_element_text(contact_page.contact_title_locator) == "Contact", "Contact page title is incorrect"


@pytest.mark.parametrize(
    "phone,gmail,location",
    [("+977 9843951178", "ghimires090@gmail.com", "Kathmandu, Nepal")]
)
def test_contact_information_is_present(driver, phone, gmail, location):
    contact_page = ContactPage(driver)
    contact_page.open_page()
    time.sleep(1)
    contact_page.click_element(contact_page.contact_locator)

    assert contact_page.get_element_text(contact_page.phone_number_locator) == phone, "Phone number is incorrect" 
    assert contact_page.get_element_text(contact_page.gmail_locator) == gmail, "Gmail is incorrect"
    assert contact_page.get_element_text(contact_page.location_locator) == location, "Location is incorrect" 


def test_contact_form_is_present(driver):
    contact_page = ContactPage(driver)
    contact_page.open_page()
    time.sleep(1)
    contact_page.click_element(contact_page.contact_locator)

    assert contact_page.is_contact_form_present(), "Contact form is not present"


def test_contact_form_submit_button_is_present(driver):
    contact_page = ContactPage(driver)
    contact_page.open_page()
    time.sleep(1)
    contact_page.click_element(contact_page.contact_locator)

    assert contact_page.is_element_present(contact_page.submit_button_locator), "Submit button is not present"


@pytest.mark.parametrize(
    "name,email,subject,message",
    [("Saroj Ghimire", "ghimires090@gmail.com", "Test Subject", "This is a test message.")]
)
def test_contact_form_submission(driver, name, email, subject, message):
    contact_page = ContactPage(driver)
    contact_page.open_page()
    time.sleep(1)
    contact_page.click_element(contact_page.contact_locator)

    # Fill the contact form
    contact_page.fill_contact_form(name, email, subject, message)
    contact_page.scroll_to_element(contact_page.submit_button_locator)
    contact_page.click_element(contact_page.submit_button_locator)
    time.sleep(2)  # Wait for the form submission to complete


