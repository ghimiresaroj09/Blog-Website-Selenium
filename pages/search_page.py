from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.search_field_locator = (By.XPATH,"//input[@name = 'q']")
        self.search_button_locator = (By.XPATH,"//button[@type = 'submit']")
        self.search_blog_body_locator = (By.XPATH,"//div[@class='post post-xl']")
        self.search_blog_category_badge_locator = (By.XPATH,".//div[@class='thumb rounded']//a[contains(@href,'/category/')]")
        self.search_blog_image_locator = (By.XPATH,".//img[contains(@src,'/media/Images/')]")
        self.search_blog_post_title_locator = (By.XPATH,".//h4[contains(@class,'post-title')]")
        self.search_blog_time_read_locator = (By.XPATH,".//li[contains(text(),'Min Read')]")
        self.search_blog_datetime_locator = (By.XPATH,".//ul[@class='meta list-inline mb-0']/li[2]")
        self.search_blog_continue_reading_locator = (By.XPATH,".//a[text() = 'Continue reading']")

        self.wait = WebDriverWait(driver, 10)

    def open_search_page(self):
        search = self.wait.until(EC.element_to_be_clickable(self.search_locator))
        search.click()

    def is_search_field_present(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_field_locator))
            return True
        except:
            return False

    def is_search_button_present(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_button_locator))
            return True
        except:
            return False
        
    def enter_search_query(self, query):
        search_field = self.wait.until(EC.visibility_of_element_located(self.search_field_locator))
        search_field.clear()
        search_field.send_keys(query)

    def click_search_button(self):
        search_button = self.wait.until(EC.element_to_be_clickable(self.search_button_locator))
        search_button.click()

    def is_search_blog_body_present(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_blog_body_locator))
            return True
        except:
            return False
        
    def is_search_blog_category_badge_present(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_category_badge_locator)
                return blog.is_displayed()
        except:
            return False


    def click_search_blog_category_badge(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_category_badge_locator)
                blog.click()
        except Exception as e:
            print(f"Failed to click category badge: {e}")


    def is_search_blog_image_present(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_image_locator)
                return blog.is_displayed()
        except:
            return False
        
    def click_search_blog_image(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_image_locator)
                blog.click()
        except Exception as e:
            print(f"Failed to click blog image: {e}")    

    def is_search_blog_post_title_present(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_post_title_locator)
                return blog.is_displayed()
        except:
            return False

    def click_search_blog_post_title(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_post_title_locator)
                blog.click()
        except Exception as e:
            print(f"Failed to click blog post title: {e}")


    def is_search_blog_time_read_present(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_time_read_locator)
                return blog.is_displayed()
        except:
            return False
        
    def is_search_blog_datetime_present(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_datetime_locator)
                return blog.is_displayed()
        except:
            return False
        
    def is_search_blog_continue_reading_present(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_continue_reading_locator)
                return blog.is_displayed()
        except:
            return False
        
    def click_search_blog_continue_reading(self):
        try:
            blogs = self.driver.find_elements(*self.search_blog_body_locator)
            if blogs:
                blog = blogs[0].find_element(*self.search_blog_continue_reading_locator)
                blog.click()
        except Exception as e:
            print(f"Failed to click continue reading: {e}")


    