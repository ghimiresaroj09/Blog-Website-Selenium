from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
import time

class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.category_title_locator = (By.XPATH,"//h1[@class = 'mt-0 mb-2']")
        self.category_blog_body_locator = (By.XPATH,"//div[@class = 'post post-grid rounded bordered']")
        self.category_blog_badge_locator = (By.XPATH,".//a[@class = 'category-badge position-absolute']")
        self.category_blog_image_locator = (By.XPATH,".//img[contains(@src,'/media/Images/')]")
        self.category_blog_title_locator = (By.XPATH,".//h5[contains(@class,'post-title')]")
        self.category_blog_read_time_locator = (By.XPATH,".//li[contains(text(),'Min Read')]")
        self.category_blog_datetime_locator = (By.XPATH,".//li[contains(text(),'Min Read')]/preceding-sibling::li[1]")

    
    def is_category_blog_present(self):
        try:
            blogs = self.driver.find_elements(*self.category_blog_body_locator)
            return len(blogs) > 0
        except NoSuchElementException:
            return False

    def is_category_blog_badge_present(self):
        try:
            blogs = self.driver.find_elements(*self.category_blog_body_locator)
            if blogs:
                badge = blogs[0].find_element(*self.category_blog_badge_locator)
                return badge.is_displayed()
        except NoSuchElementException:
            return False
        
    def is_blog_image_present(self):
        try:
            blogs = self.driver.find_elements(*self.category_blog_body_locator)
            if blogs:
                image = blogs[0].find_element(*self.category_blog_image_locator)
                return image.is_displayed()
        except NoSuchElementException:
            return False

    def is_blog_title_present(self):
        try:
            blogs = self.driver.find_elements(*self.category_blog_body_locator)
            if blogs:
                title = blogs[0].find_element(*self.category_blog_title_locator)
                return title.is_displayed()
            return False
        except NoSuchElementException:
            return False
        
    def is_blog_read_time_present(self):
        try:
            blogs = self.driver.find_elements(*self.category_blog_body_locator)
            if blogs:
                read_time = blogs[0].find_element(*self.category_blog_read_time_locator)
                return read_time.is_displayed()
            return False
        except NoSuchElementException:
            return False
        
    def is_blog_datetime_present(self):
        try:
            blogs = self.driver.find_elements(*self.category_blog_body_locator)
            if blogs:
                datetime = blogs[0].find_element(*self.category_blog_datetime_locator)
                return datetime.is_displayed()
            return False
        except NoSuchElementException:
            return False
        
    def click_blog_title(self):
        try:
            blogs = self.driver.find_elements(*self.category_blog_body_locator)
            if blogs:
                title = blogs[0].find_element(*self.category_blog_title_locator)
                title.click()
            else:
                print("No blog elements found.")
        except NoSuchElementException:
            print("Blog title not found.")

    def click_blog_image(self):
        try:
            blogs = self.driver.find_elements(*self.category_blog_body_locator)
            if blogs:
                image = blogs[0].find_element(*self.category_blog_image_locator)
                image.click()
            else:
                print("No blog elements found.")
        except NoSuchElementException:
            print("Blog image not found.")

    def click_blog_badge(self):
        try:
            blogs = self.driver.find_elements(*self.category_blog_body_locator)
            if blogs:
                badge = blogs[0].find_element(*self.category_blog_badge_locator)
                badge.click()
            else:
                print("No blog elements found.")
        except NoSuchElementException:
            print("Blog badge not found.")