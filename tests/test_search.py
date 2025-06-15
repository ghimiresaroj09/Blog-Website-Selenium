import time
import pytest
from selenium.webdriver.common.by import By
from pages.blog_details import BlogDetailPage
from pages.search_page import SearchPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.category_page import CategoryPage


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_page(driver, query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    assert query in search_page.get_element_text(search_page.search_blog_post_title_locator), "Search page title is incorrect"

def test_search_field_present(driver):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)

    assert search_page.is_search_field_present(), "Search field is not present"


def test_search_button_present(driver):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)

    assert search_page.is_search_button_present(), "Search button is not present"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_body_present(driver, query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    assert search_page.is_search_blog_body_present(), "Search blog body is not present"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_category_badge_present(driver,query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    assert search_page.is_search_blog_category_badge_present(), "Search blog category badge is not present"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_category_badge_click(driver, query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)
    badge_text = search_page.get_element_text(search_page.search_blog_category_badge_locator)
    search_page.click_search_blog_category_badge()
    time.sleep(1)

    category_page = CategoryPage(driver)
    category_text = search_page.get_element_text(category_page.category_title_locator)
    assert badge_text == category_text, "Category badge text does not match category title text"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_image_present(driver,query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    assert search_page.is_search_blog_image_present(), "Search blog image is not present"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_image_click(driver, query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    search_page.scroll_to_element(search_page.search_blog_image_locator)
    blog_image_element = driver.find_element(*search_page.search_blog_image_locator)
    image_before = blog_image_element.get_attribute("src")
    search_page.click_search_blog_image()
    time.sleep(1)
    blog_detail_page = BlogDetailPage(driver)
    opened_image_element = driver.find_element(*blog_detail_page.image_locator)
    image_after = opened_image_element.get_attribute("src")

    assert image_before == image_after, "Blog image is not present or has changed after clicking"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_title_present(driver, query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    assert search_page.is_search_blog_post_title_present(), "Search blog title is not present"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_title_click(driver,query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    search_page.scroll_to_element(search_page.search_blog_post_title_locator)
    search_blog_title = search_page.get_element_text(search_page.search_blog_post_title_locator)
    search_page.click_search_blog_post_title()
    time.sleep(1)

    blog_detail_page = BlogDetailPage(driver)
    blog_title = search_page.get_element_text(blog_detail_page.title_locator)

    assert search_blog_title[:45] in blog_title, "Blog title does not match after clicking"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_time_read_present(driver,query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    assert search_page.is_search_blog_time_read_present(), "Search blog read time is not present"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_datetime_present(driver,query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    assert search_page.is_search_blog_datetime_present(), "Search blog date time is not present"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_continue_reading_present(driver,query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    assert search_page.is_search_blog_continue_reading_present(), "Search blog continue reading button is not present"


@pytest.mark.parametrize("query", ["5G Technology"])
def test_search_blog_continue_reading_click(driver,query):
    search_page = SearchPage(driver)
    search_page.open_page()
    time.sleep(1)
    search_page.open_search_page()
    time.sleep(1)
    search_page.enter_search_query(query)
    search_page.click_search_button()
    time.sleep(1)

    search_page.scroll_to_element(search_page.search_blog_continue_reading_locator)
    search_page.click_search_blog_continue_reading()
    time.sleep(1)

    blog_detail_page = BlogDetailPage(driver)
    blog_title = search_page.get_element_text(blog_detail_page.title_locator)

    assert blog_title, "Blog title is not present after clicking continue reading"


