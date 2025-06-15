from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.contact_title_locator = (By.XPATH,"//h1[@class = 'mt-0 mb-2']")
        self.phone_number_locator = (By.XPATH,"//h3[text()='Phone']/following-sibling::p")
        self.gmail_locator = (By.XPATH,"//h3[text()='Gmail']/following-sibling::p")
        self.location_locator = (By.XPATH,"//h3[text()='Location']/following-sibling::p")
        self.name_field_locator = (By.XPATH,"//input[@id = 'InputName']")
        self.email_field_locator = (By.XPATH,"//input[@id = 'email']")
        self.subject_field_locator = (By.XPATH,"//input[@id = 'subject']")
        self.message_field_locator = (By.XPATH,"//textarea[@id = 'message']")
        self.submit_button_locator = (By.XPATH,"//button[@id='submit']")

    def is_contact_form_present(self):
        return (
            self.is_element_present(self.contact_title_locator) and
            self.is_element_present(self.name_field_locator) and
            self.is_element_present(self.email_field_locator) and
            self.is_element_present(self.subject_field_locator) and
            self.is_element_present(self.message_field_locator)
        )
   

    def fill_contact_form(self, name, email, subject, message):
        self.enter_text(self.name_field_locator, name)
        self.enter_text(self.email_field_locator, email)
        self.enter_text(self.subject_field_locator, subject)
        self.enter_text(self.message_field_locator, message)
        time.sleep(2) 

