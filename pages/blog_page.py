from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BlogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        ##carausel
        self.carausel_locator = (By.XPATH,"//div[contains(@class,'post featured-post-xl slick-slide')]")
        self.carausel_category_locator = (By.XPATH,"//a[contains(@href, '/category/') and @class = 'category-badge lg']")
        self.carausel_images_locator = (By.XPATH,"//div[contains(@data-bg-image, '/media/Images')]")
        self.carausel_post_title_locator = (By.XPATH,"//h4[@class = 'post-title']")
        self.carausel_time_read_locator = (By.XPATH,"//a[contains(text(),'Min Read')]")
        self.carausel_datetime_locator = (By.XPATH,"//a[contains(text(),'Min Read')]/ancestor::li/following-sibling::li[1]")
        self.carausel_next_locator = (By.XPATH,"//button[@aria-label = 'Next']")
        self.carausel_previous_locator = (By.XPATH,"//button[@aria-label = 'Previous']")
        self.carausel_change_button_locator = (By.XPATH,"//li[contains(@id,'slick-slide')]/button")

        #blog
        self.blog_body_locator = (By.XPATH,"//div[@class = 'post post-classic rounded bordered']")
        self.blog_category_badge_locator = (By.XPATH,".//a[contains(@href,'/category/')]")
        self.blog_image_locator = (By.XPATH,".//img[contains(@src,'/media/Images/')]")
        self.blog_post_title_locator = (By.XPATH,".//h5[contains(@class,'post-title')]")
        self.blog_time_read_locator = (By.XPATH,".//li[contains(text(),'Min Read')]")
        self.blog_datetime_locator = (By.XPATH,".//li[contains(text(),'Min Read')]/preceding-sibling::li[1]")
        self.blog_continue_reading_locator = (By.XPATH,".//a[text() = 'Continue reading']")

        #Side Tab
        self.popular_tab_locator = (By.XPATH,"//button[text() = 'Popular']")
        self.important_tab_locator = (By.XPATH,"//button[text() = 'Important']")
        self.sidetab_blog_body_locator = (By.XPATH,"//div[@class = 'post post-list-sm circle']")
        self.sidetab_blog_image_locator = (By.XPATH,".//img[contains(@src,'/media/Images/')]")
        self.sidetab_blog_title_locator = (By.XPATH,".//h6[contains(@class,'post-title')]")
        self.sidetab_blog_datetime_locator = (By.XPATH,".//ul[@class='meta list-inline mt-1 mb-0']/li")

        #Pagination
        self.next_page_locator = (By.XPATH,"//a[text() = '2']")

        self.wait = WebDriverWait(driver, 10)

    def is_carausel_present(self):
        try:
            carausel = self.driver.find_element(*self.carausel_locator)
            return carausel.is_displayed()
        except NoSuchElementException:
            return False

    def is_carausel_category_present(self):
        try:
            categories = self.driver.find_elements(*self.carausel_category_locator)
            return len(categories) > 0 and categories[0].is_displayed()
        except NoSuchElementException:
            return False
        
    def click_carausel_category(self):
        try:
            categories = self.driver.find_elements(*self.carausel_category_locator)
            if categories:
                categories[0].click()
                return True
            return False
        except NoSuchElementException:
            return False    
        
    def is_carausel_image_present(self):
        try:
            images = self.driver.find_elements(*self.carausel_images_locator)
            return len(images) > 0 and images[0].is_displayed()
        except NoSuchElementException:
            return False
        
    def click_carausel_image(self):
        try:
            images = self.driver.find_elements(*self.carausel_images_locator)
            if images:
                self.driver.execute_script("arguments[0].click();", images[0])
                return True
            return False
        except NoSuchElementException:
            return False
        
    def is_carausel_title_present(self):
        try:
            titles = self.driver.find_elements(*self.carausel_post_title_locator)
            return len(titles) > 0 and titles[0].is_displayed()
        except NoSuchElementException:
            return False
        
    def click_carausel_title(self):
        try:
            titles = self.driver.find_elements(*self.carausel_post_title_locator)
            if titles:
                titles[0].click()
                return True
            return False
        except NoSuchElementException:
            return False
        
    def is_carausel_time_read_present(self):
        try:
            times = self.driver.find_elements(*self.carausel_time_read_locator)
            return len(times) > 0 and times[0].is_displayed()
        except NoSuchElementException:
            return False
        
    def is_carausel_datetime_present(self):
        try:
            datetimes = self.driver.find_elements(*self.carausel_datetime_locator)
            return len(datetimes) > 0 and datetimes[0].is_displayed()
        except NoSuchElementException:
            return False
    
    def is_carausel_next_button_present(self):
        try:
            next_button = self.driver.find_element(*self.carausel_next_locator)
            return next_button.is_displayed() and next_button.is_enabled()
        except NoSuchElementException:
            return False

    def click_carausel_next_button(self):
        try:
            next_button = self.driver.find_element(*self.carausel_next_locator)
            next_button.click()
            return True
        except NoSuchElementException:
            return False

    def is_carausel_previous_button_present(self):
        try:
            previous_button = self.driver.find_element(*self.carausel_previous_locator)
            return previous_button.is_displayed() and previous_button.is_enabled()
        except NoSuchElementException:
            return False
        
    def click_carausel_previous_button(self):
        try:
            previous_button = self.driver.find_element(*self.carausel_previous_locator)
            previous_button.click()
            return True
        except NoSuchElementException:
            return False

    def is_carausel_change_button_present(self):
        try:
            change_buttons = self.driver.find_elements(*self.carausel_change_button_locator)
            return len(change_buttons) > 1 and change_buttons[1].is_displayed() and change_buttons[1].is_enabled()
        except NoSuchElementException:
            return False
         
    def click_carausel_change_button(self):
        try:
            change_buttons = self.driver.find_elements(*self.carausel_change_button_locator)
            if change_buttons:
                change_buttons[1].click()
                return True
            return False
        except NoSuchElementException:
            return False
        
    def is_blog_category_badge_present(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            if blogs:
                badge = blogs[0].find_element(*self.blog_category_badge_locator)
                return badge.is_displayed()
            return False
        except NoSuchElementException:
            return False
        
    def click_blog_category_badge(self):
        try:
            blogs = WebDriverWait(self.driver, 10).until(
                lambda d: d.find_elements(*self.blog_body_locator)
            )
            if blogs:
                badge = blogs[0].find_element(*self.blog_category_badge_locator)

                # Scroll into view
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", badge)

                # Optional wait to ensure layout stabilizes
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(badge))

                # JavaScript click to bypass overlays
                self.driver.execute_script("arguments[0].click();", badge)

                return True
            return False

        except (NoSuchElementException, TimeoutException):
            return False
        
    def is_blog_image_present(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            if blogs:
                image = blogs[0].find_element(*self.blog_image_locator)
                return image.is_displayed()
            return False
        except NoSuchElementException:
            return False
        
    def click_blog_image(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            if blogs:
                image = blogs[0].find_element(*self.blog_image_locator)
                image.click()
                return True
            return False
        except NoSuchElementException:
            return False    
        
    def is_blog_title_present(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            if blogs:
                title = blogs[0].find_element(*self.blog_post_title_locator)
                return title.is_displayed()
            return False
        except NoSuchElementException:
            return False
        
    def click_blog_title(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            if blogs:
                title = blogs[0].find_element(*self.blog_post_title_locator)
                title.click()
                return True
            return False
        except NoSuchElementException:
            return False    
        
    def is_blog_time_read_present(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            if blogs:
                time_read = blogs[0].find_element(*self.blog_time_read_locator)
                return time_read.is_displayed()
            return False
        except NoSuchElementException:
            return False
        
    def is_blog_datetime_present(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            if blogs:
                datetime = blogs[0].find_element(*self.blog_datetime_locator)
                return datetime.is_displayed()
            return False
        except NoSuchElementException:
            return False

    def is_continue_reading_button_present(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            if blogs:
                continue_reading = blogs[0].find_element(*self.blog_continue_reading_locator)
                return continue_reading.is_displayed() and continue_reading.is_enabled()
            return False
        except NoSuchElementException:
            return False

    def click_continue_reading_button(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            if blogs:
                continue_reading = blogs[0].find_element(*self.blog_continue_reading_locator)
                continue_reading.click()
                return True
            return False
        except NoSuchElementException:
            return False
        
    def is_pagination_present(self):
        try:
            next_page = self.driver.find_element(*self.next_page_locator)
            return next_page.is_displayed() and next_page.is_enabled()
        except NoSuchElementException:
            return False
        
    def click_pagination_next_page(self):
        try:
            next_page = self.driver.find_element(*self.next_page_locator)
            next_page.click()
            return True
        except NoSuchElementException:
            return False
        
    def get_total_blogs(self):
        try:
            blogs = self.driver.find_elements(*self.blog_body_locator)
            return len(blogs)
        except NoSuchElementException:
            return 0

    def is_sidetab_popular_present(self):
        try:
            popular_tab = self.driver.find_element(*self.popular_tab_locator)
            return popular_tab.is_displayed() and popular_tab.is_enabled()
        except NoSuchElementException:
            return False

    def click_sidetab_popular(self):
        try:
            popular_tab = self.driver.find_element(*self.popular_tab_locator)
            popular_tab.click()
            return True
        except NoSuchElementException:
            return False

    def is_sidetab_important_present(self):
        try:
            important_tab = self.driver.find_element(*self.important_tab_locator)
            return important_tab.is_displayed() and important_tab.is_enabled()
        except NoSuchElementException:
            return False

    def click_sidetab_important(self):
        try:
            important_tab = self.driver.find_element(*self.important_tab_locator)
            important_tab.click()
            return True
        except NoSuchElementException:
            return False
        
    def is_sidetab_blog_present(self):
        try:
            blogs = self.driver.find_elements(*self.sidetab_blog_body_locator)
            return len(blogs) > 0 and blogs[0].is_displayed()
        except NoSuchElementException:
            return False
        
        
    def click_sidetab_blog_by_title(self):
        blogs = self.driver.find_elements(*self.sidetab_blog_body_locator)
        try:
            if blogs:
                title = blogs[0].find_element(*self.sidetab_blog_title_locator)
                title.click()
                return True
            return False
        except NoSuchElementException:
            return False

    def click_sidetab_blog_by_image(self):
        blogs = self.driver.find_elements(*self.sidetab_blog_body_locator)
        try:
            if blogs:
                image = blogs[0].find_element(*self.sidetab_blog_image_locator)
                image.click()
                return True
            return False
        except NoSuchElementException:
            return False