import time
import pytest
from selenium.webdriver.common.by import By
from pages.blog_details import BlogDetailPage
from pages.blog_page import BlogPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from slugify import slugify

from pages.category_page import CategoryPage

def test_is_caraousel_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_carausel_present(), "Carousel is not present"


def test_is_carausel_category_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_carausel_category_present(), "Carousel category is not present"


def test_carausel_category_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)
    blog_page.click_carausel_category()


def test_carausel_image_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_carausel_image_present(), "Carousel image is not present"


def test_carausel_image_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(2)
    blog_page.click_carausel_image()


def test_carausel_title_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_carausel_title_present(), "Carousel title is not present"


def test_carausel_title_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)
    blog_page.click_carausel_title()


def test_carausel_time_read_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_carausel_time_read_present(), "Carousel read time is not present"


def test_carausel_datetime_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_carausel_datetime_present(), "Carousel date time is not present"


def test_carausel_next_button_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_carausel_next_button_present(), "Carousel next button is not present"

def test_carausel_next_button_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)
    blogs = driver.find_elements(*blog_page.carausel_locator)

    for _ in range(len(blogs) - 1):
        blog_page.click_carausel_next_button()
        time.sleep(1.5)

def test_carausel_previous_button_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_carausel_previous_button_present(), "Carousel previous button is not present"


def test_carausel_previous_button_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)
    blogs = driver.find_elements(*blog_page.carausel_locator)

    for _ in range(len(blogs) - 1):
        blog_page.click_carausel_previous_button()
        time.sleep(1.5)


def test_carausel_change_button_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_carausel_change_button_present(), "Carousel change button is not present"
    

def test_carausel_change_button_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)
    blog_page.click_carausel_change_button()
    time.sleep(1)


def test_is_blog_category_badge_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_blog_category_badge_present(), "Blog category badge is not present"


def test_blog_category_badge_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)
    
    blog_page.click_blog_category_badge()
    time.sleep(1)

    category_page = CategoryPage(driver)
    category_title = blog_page.get_element_text(category_page.category_title_locator)

    assert category_title, "Category title is not present"
    

def test_is_blog_image_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_blog_image_present(), "Blog image is not present"


def test_blog_image_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(2)
    blog_page.scroll_to_element(blog_page.blog_image_locator)
    blog_page.click_blog_image()
    time.sleep(1)
    blog_detail_page = BlogDetailPage(driver)
    blog_title = blog_page.get_element_text(blog_detail_page.title_locator)
    assert blog_title, "Blog title is not present"
    

def test_is_blog_title_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_blog_title_present(), "Blog title is not present"


def test_blog_title_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(2)
    blog_page.scroll_to_element(blog_page.blog_post_title_locator)
    blog_page.click_blog_title()
    time.sleep(1)
    blog_detail_page = BlogDetailPage(driver)
    blog_title = blog_page.get_element_text(blog_detail_page.title_locator)
    assert blog_title, "Blog title is not present"

def test_is_blog_read_time_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_blog_time_read_present(), "Blog read time is not present"


def test_blog_datetime_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_blog_datetime_present(), "Blog date time is not present"


def test_is_continue_reading_button_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_continue_reading_button_present(), "Continue reading button is not present"


def test_continue_reading_button_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(2)
    blog_page.scroll_to_element(blog_page.blog_continue_reading_locator)
    blog_page.click_continue_reading_button()
    time.sleep(1)
    blog_detail_page = BlogDetailPage(driver)
    blog_title = blog_page.get_element_text(blog_detail_page.title_locator)
    assert blog_title, "Blog title is not present"


def test_is_pagination_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_pagination_present(), "Pagination is not present"

def test_pagination_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)
    blog_page.scroll_to_element(blog_page.next_page_locator)
    blog_page.click_pagination_next_page()
    time.sleep(1)

    assert "page=2" in driver.current_url, "Pagination did not navigate to the next page"

def test_total_blogs_count(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    total_blogs = blog_page.get_total_blogs()
    assert total_blogs > 0, "Total blogs count should be greater than zero"
    assert total_blogs <= 5, "Total blogs count should be equal or less than 5"


def test_sidetab_popular_blogs_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_sidetab_blog_present, "Popular blogs section is not present"


def test_sidetab_popular_blogs_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(2)
    blog_page.scroll_to_element(blog_page.popular_tab_locator)
    blog_page.click_sidetab_popular()
    time.sleep(1)


def test_sidetab_important_blogs_present(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(1)

    assert blog_page.is_sidetab_important_present(), "Important blogs section is not present"


def test_sidetab_important_blogs_click(driver):
    blog_page = BlogPage(driver)
    blog_page.open_page()
    time.sleep(2)
    blog_page.scroll_to_element(blog_page.important_tab_locator)
    blog_page.click_sidetab_important()
    time.sleep(1)

