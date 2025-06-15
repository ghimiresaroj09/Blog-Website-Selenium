import time
import pytest
from slugify import slugify
from pages.category_page import CategoryPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("submenu", ["Nature"])
def test_category_page(driver, submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)
    time.sleep(1)

    assert category_page.get_element_text(category_page.category_title_locator) == submenu, "Category page title is incorrect"


@pytest.mark.parametrize("submenu", ["Nature"])
def test_category_blog_is_present(driver, submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)

    assert category_page.is_category_blog_present(), "Category blog is not present"


@pytest.mark.parametrize("submenu", ["Nature"])
def test_category_blog_badge_present(driver,submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)

    assert category_page.is_category_blog_badge_present(), "Category blog badge is not present"
    assert category_page.get_element_text(category_page.category_blog_badge_locator) == submenu, "Category blog badge text is incorrect"


@pytest.mark.parametrize("submenu", ["Nature"])
def test_category_blog_image_present(driver, submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)

    assert category_page.is_blog_image_present(), "Category blog image is not present"


@pytest.mark.parametrize("submenu", ["Nature"])
def test_category_blog_title_present(driver, submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)

    assert category_page.is_blog_title_present(), "Category blog title is not present"


@pytest.mark.parametrize("submenu", ["Nature"])
def test_category_blog_read_time_present(driver,submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)

    assert category_page.is_blog_read_time_present(), "Category blog read time is not present"


@pytest.mark.parametrize("submenu", ["Nature"])
def test_category_blog_datetime_present(driver, submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)

    assert category_page.is_blog_datetime_present(), "Category blog datetime is not present"


@pytest.mark.parametrize("submenu", ["Nature"])
def test_click_blog_title(driver,submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)
    time.sleep(1)
    category_page.click_blog_title()
    time.sleep(1)
    blog_title = category_page.get_element_text(category_page.category_blog_title_locator)
    expected_slug = slugify(blog_title)

    assert expected_slug in driver.current_url, f"Expected slug '{expected_slug}' not found in URL: {driver.current_url}"


@pytest.mark.parametrize("submenu", ["Nature"])
def test_click_blog_image(driver, submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)
    time.sleep(1)
    category_page.click_blog_image()
    time.sleep(1)
    blog_title = category_page.get_element_text(category_page.category_blog_title_locator)
    expected_slug = slugify(blog_title)

    assert expected_slug in driver.current_url, f"Expected slug '{expected_slug}' not found in URL: {driver.current_url}"


@pytest.mark.parametrize("submenu", ["Nature"])
def test_category_blog_badge_click(driver, submenu):
    category_page = CategoryPage(driver)
    category_page.open_page()
    time.sleep(1)
    category_page.click_category(submenu)
    time.sleep(1)
    category_page.click_blog_badge()
    time.sleep(1)

    assert category_page.get_element_text(category_page.category_title_locator) == submenu, "Category page title is incorrect"