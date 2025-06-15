from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from pages.blog_page import BlogPage

class BlogDetailPage(BlogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        ##Post
        self.image_locator = (By.XPATH,"//img[contains(@src,'/media/Images/')]")
        self.title_locator = (By.XPATH,"//h2[contains(@class,'post-title')]")
        self.read_time_locator = (By.XPATH,"//li[contains(text(),'Min Read')]")
        self.datetime_locator = (By.XPATH,"//li[contains(text(),'Min Read')]/preceding-sibling::li[1]")

        ##Comments
        self.total_comments_locator = (By.XPATH,"//h3[contains(text(),'Comments')]")
        self.comment_field_locator = (By.XPATH,"//textarea[@id='InputComment']")
        self.email_field_locator = (By.XPATH,"//input[@id='InputEmail']")
        self.website_field_locator = (By.XPATH,"//input[@id='InputWeb']")
        self.name_field_locator = (By.XPATH,"//input[@id='InputName']")
        self.submit_locator = (By.XPATH,"//button[@id='submit']")
        self.comment_box_locator = (By.XPATH,"//ul[@class='comments']/li[@class='comment rounded']")
        self.comment_user_image_locator = (By.XPATH,".//div[@class='thumb']/img")
        self.comment_user_name_locator = (By.XPATH,".//h4[@class='name']/a")
        self.commnt_datetime_locator = (By.XPATH,".//span[@class='date']")
        self.user_comment_locator = (By.XPATH,".//h4[@class='name']/a//following::p")

    def is_blog_image_present(self):
        try:
            image = self.driver.find_element(*self.image_locator)
            return image.is_displayed()
        except NoSuchElementException:
            return False
        
    def is_blog_title_present(self):
        try:
            title = self.driver.find_element(*self.title_locator)
            return title.is_displayed()
        except NoSuchElementException:
            return False
        
    def is_blog_read_time_present(self):
        try:
            read_time = self.driver.find_element(*self.read_time_locator)
            return read_time.is_displayed()
        except NoSuchElementException:
            return False
        
    def is_blog_datetime_present(self):
        try:
            datetime = self.driver.find_element(*self.datetime_locator)
            return datetime.is_displayed()
        except NoSuchElementException:
            return False
        
    def get_total_comments(self):
        try:
            total_comments = self.driver.find_element(*self.total_comments_locator).text
            num = int(total_comments.split('(')[1].split(')')[0])
            return num
        except NoSuchElementException:
            return 0
        
    def is_comment_form_present(self):
        return (
            self.is_element_present(self.comment_field_locator) and
            self.is_element_present(self.email_field_locator) and
            self.is_element_present(self.website_field_locator) and
            self.is_element_present(self.name_field_locator) and
            self.is_element_present(self.submit_locator)
        )

    def fill_comment_form(self, comment, email, website, name):
        self.enter_text(self.comment_field_locator, comment)
        self.enter_text(self.email_field_locator, email)
        self.enter_text(self.website_field_locator, website)
        self.enter_text(self.name_field_locator, name)
        time.sleep(2)


    def is_comment_user_image_present(self):
        try:
            comments = self.driver.find_elements(*self.comment_box_locator)
            if comments:
                image = comments[0].find_element(*self.comment_user_image_locator)
                return image.is_displayed()
            return False
        except NoSuchElementException:
            return False

    def is_comment_user_name_present(self):
        try:
            comments = self.driver.find_elements(*self.comment_box_locator)
            if comments:
                username = comments[0].find_element(*self.comment_user_name_locator)
                return username.is_displayed()
            return False
        except NoSuchElementException:
            return False
        
    def is_comment_datetime_present(self):
        try:
            comments = self.driver.find_elements(*self.comment_box_locator)
            if comments:
                datetime = comments[0].find_element(*self.commnt_datetime_locator)
                return datetime.is_displayed()
            return False
        except NoSuchElementException:
            return False
        
    def is_user_comment_present(self):
        try:
            comments = self.driver.find_elements(*self.comment_box_locator)
            if comments:
                user_comment = comments[0].find_element(*self.user_comment_locator)
                return user_comment.is_displayed()
            return False
        except NoSuchElementException:
            return False
        

    def click_sidetab_category_submenu(self, submenu):
        self.sidetab_category_submenu_locator = (By.XPATH,f"(//a[text() = '{submenu}'])[3]")
        try:
            self.scroll_to_element(self.sidetab_category_submenu_locator)
            element = self.wait.until(EC.element_to_be_clickable(self.sidetab_category_submenu_locator))
            element.click()
            return True
        except NoSuchElementException:
            return False
        
