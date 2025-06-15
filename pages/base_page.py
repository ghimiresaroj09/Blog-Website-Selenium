from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logo_locator = (By.XPATH,"(//a[@class = 'navbar-brand'])[2]")
        self.blog_locator = (By.XPATH,"(//a[text() = 'Blog'])[2]")
        self.category_locator = (By.XPATH,"(//a[contains(text(),'Category')])[2]")
        # self.category_submenu_locator = (By.XPATH,"(//a[text() = 'Nature'])[2]")
        self.contact_locator = (By.XPATH,"(//a[text() = 'Contact'])[2]")
        self.header_facebook_locator = (By.XPATH,"(//a[contains(@href,'facebook')])[2]")
        self.header_instagram_locator = (By.XPATH,"(//a[contains(@href,'instagram')])[2]")
        self.header_twitter_locator = (By.XPATH,"(//a[contains(@href,'x')])[2]")
        self.search_locator = (By.XPATH,"(//button[@class = 'search icon-button'])[2]")
        self.burger_menu_locator = (By.XPATH,"(//button[@class = 'burger-menu icon-button'])[2]")

        ##Sidebar
        self.sidebar_close_locator = (By.XPATH,"(//button[@class = 'btn-close'])[2]")
        self.sidebar_logo_locator = (By.XPATH,"(//img[contains(@src,'S.png')])[3]")
        self.sidebar_blog_locator = (By.XPATH,"(//a[text() = 'Blog'])[3]")
        self.sidebar_category_open_locator = (By.XPATH,"//i[@class = 'icon-arrow-down switch']")
        self.sidebar_category_submenu_locator = (By.XPATH,"(//a[text() = 'Nature'])[4]")
        self.sidebar_contact_locator = (By.XPATH,"(//a[text() = 'Contact'])[3]")
        self.sidebar_facebook_locator = (By.XPATH,"(//a[contains(@href,'facebook')])[4]")
        self.sidebar_instagram_locator = (By.XPATH,"(//a[contains(@href,'instagram')])[4]")
        self.sidebar_twitter_locator = (By.XPATH,"(//a[contains(@href,'x')])[4]")

        ##Footer
        self.footer_copyright_locator = (By.XPATH,"//span[@class = 'copyright']")
        self.footer_facebook_locator = (By.XPATH,"(//a[contains(@href,'facebook')])[2]")
        self.footer_instagram_locator = (By.XPATH,"(//a[contains(@href,'instagram')])[2]")
        self.footer_twitter_locator = (By.XPATH,"(//a[contains(@href,'x')])[2]")
        self.backtotop_locator = (By.XPATH,"//a[@id  = 'return-to-top']")
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", *self.backtotop_locator)

        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def open_page(self):
        self.driver.get("http://127.0.0.1:8000/")

    def click_category(self, submenu):
        self.category_submenu_locator = (By.XPATH, f"(//a[text() = '{submenu}'])[2]")
        dropdown = self.wait.until(EC.visibility_of_element_located(self.category_locator))
        self.action.move_to_element(dropdown).perform()
        submenu_element = self.wait.until(EC.visibility_of_element_located(self.category_submenu_locator))
        submenu_element.click()


    def click_sidebar_category_open(self):
        self.driver.find_element(*self.sidebar_category_open_locator).click()
        submenu = self.wait.until(EC.visibility_of_element_located(self.sidebar_category_submenu_locator))
        submenu.click()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)

    def wait_for_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(f"Element {locator} not found: {e}")
            return None
        
    def is_element_present(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed() and element.is_enabled()
        except Exception as e:
            print(f"Field {locator} not ready: {e}")
            return False
        
    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"Failed to click element {locator}: {e}")

    def enter_text(self, locator, text):
        try:
            field = self.wait.until(EC.visibility_of_element_located(locator))
            field.clear()
            field.send_keys(text)
        except Exception as e:
            print(f"Failed to enter text in element {locator}: {e}")

    def get_element_text(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except Exception as e:
            print(f"Failed to get text from element {locator}: {e}")
            return ""
    
        
        