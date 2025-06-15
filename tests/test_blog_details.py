import time
import pytest
from selenium.webdriver.common.by import By
from pages.blog_details import BlogDetailPage
from pages.category_page import CategoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from slugify import slugify

def test_blog_details_page(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.title_locator)
    blog_title = blog_detail_page.get_element_text(blog_detail_page.title_locator)
    expected_slug = slugify(blog_title)

    assert expected_slug in driver.current_url, f"Expected slug '{expected_slug}' not found in URL: {driver.current_url}"


def test_blog_details_image_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_image_locator)
    blog_image_element = driver.find_element(*blog_detail_page.blog_image_locator)
    image_before = blog_image_element.get_attribute("src")
    blog_detail_page.click_blog_image()
    time.sleep(1)

    opened_image_element = driver.find_element(*blog_detail_page.image_locator)
    image_after = opened_image_element.get_attribute("src")

    assert image_before == image_after, "Blog image is not present or has changed after clicking"


def test_blog_details_title_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)

    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)

    # Capture title text BEFORE clicking
    title_before_click = blog_detail_page.get_element_text(blog_detail_page.blog_post_title_locator)
    print("Blog post title text:", title_before_click)

    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.title_locator)
    title_after_click = blog_detail_page.get_element_text(blog_detail_page.title_locator)
    print("Blog title text:", title_after_click)
    time.sleep(1)

    assert blog_detail_page.is_blog_title_present(), "Blog title is not present"
    assert title_after_click != "", "Blog title text is empty"
    assert title_after_click == title_before_click, "Blog title text does not match the post title"


def test_blog_details_read_time_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.read_time_locator)
    time.sleep(1)

    assert blog_detail_page.is_blog_read_time_present(), "Blog read time is not present"
    assert blog_detail_page.get_element_text(blog_detail_page.read_time_locator) != "", "Blog read time text is empty"
    assert blog_detail_page.get_element_text(blog_detail_page.read_time_locator) == blog_detail_page.get_element_text(blog_detail_page.blog_time_read_locator), "Blog read time text does not match the post read time"


def test_blog_details_datetime_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.datetime_locator)
    time.sleep(1)

    assert blog_detail_page.is_blog_datetime_present(), "Blog datetime is not present"
    assert blog_detail_page.get_element_text(blog_detail_page.datetime_locator) != "", "Blog datetime text is empty"
    assert blog_detail_page.get_element_text(blog_detail_page.datetime_locator) == blog_detail_page.get_element_text(blog_detail_page.blog_datetime_locator), "Blog datetime text does not match the post datetime"


def test_comments_form_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.comment_field_locator)
    time.sleep(1)
    assert blog_detail_page.is_comment_form_present(), "Comment form is not present"


def test_comment_submission(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.comment_field_locator)
    time.sleep(1)

    blog_detail_page.fill_comment_form("Test Comment", "test@gmail.com", "https://example.com", "Test User")
    blog_detail_page.scroll_to_element(blog_detail_page.submit_locator)
    blog_detail_page.click_element(blog_detail_page.submit_locator)
    time.sleep(2)


def test_comment_user_image_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.comment_user_image_locator)
    time.sleep(1)

    assert blog_detail_page.is_comment_user_image_present(), "Comment user image is not present"


def test_comment_user_name_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.comment_user_name_locator)
    time.sleep(1)

    assert blog_detail_page.is_comment_user_name_present(), "Comment user name is not present"
    assert blog_detail_page.get_element_text(blog_detail_page.comment_user_name_locator) != "", "Comment user name text is empty"


def test_comment_datetime_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.commnt_datetime_locator)
    time.sleep(1)

    assert blog_detail_page.is_comment_datetime_present, "Comment user email is not present"
    assert blog_detail_page.get_element_text(blog_detail_page.comment_box_locator) != "", "Comment user email text is empty"


def test_comment_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.user_comment_locator)
    time.sleep(1)

    assert blog_detail_page.is_user_comment_present(), "Comment user text is not present"
    assert blog_detail_page.get_element_text(blog_detail_page.user_comment_locator) != "", "Comment user text is empty"


def test_total_comments_count_increment(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    blog_detail_page.scroll_to_element(blog_detail_page.total_comments_locator)
    time.sleep(1)
    initial_count = blog_detail_page.get_total_comments()

    blog_detail_page.fill_comment_form("Test Comment", "test@gmail.com", "https://example.com", "Test User")
    blog_detail_page.scroll_to_element(blog_detail_page.submit_locator)
    blog_detail_page.click_element(blog_detail_page.submit_locator)
    time.sleep(2)
    updated_count = blog_detail_page.get_total_comments()
    assert updated_count == initial_count + 1, f"Total comments count did not increment. Expected {initial_count + 1}, got {updated_count}"


def test_blog_details_sidetab_category_submenu_click(driver):
    blog_detail_page = BlogDetailPage(driver)
    category_page = CategoryPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    submenu = "Nature"
    blog_detail_page.click_sidetab_category_submenu(submenu)
    time.sleep(1)

    assert category_page.get_element_text(category_page.category_title_locator) == submenu, "Category page title is incorrect"


def test_sidetab_blog_present(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.sidebar_blog_locator)

    assert blog_detail_page.is_sidetab_blog_present(), "Sidebar blog is not present"

def test_five_or_less_sidetab_blogs(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.sidebar_blog_locator)

    sidebar_blogs = driver.find_elements(*blog_detail_page.sidebar_blog_locator)
    assert len(sidebar_blogs) <= 5, f"Expected 5 or fewer sidebar blogs, found {len(sidebar_blogs)}"


def test_sidetab_blog_title_click(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.sidetab_blog_title_locator)
    blog_title = blog_detail_page.get_element_text(blog_detail_page.sidetab_blog_title_locator)
    blog_detail_page.click_sidetab_blog_by_title()
    time.sleep(1)

    expected_slug = slugify(blog_title)

    assert expected_slug in driver.current_url, f"Expected slug '{expected_slug}' not found in URL: {driver.current_url}"


def test_sidebar_blog_image_click(driver):
    blog_detail_page = BlogDetailPage(driver)
    blog_detail_page.open_page()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.blog_post_title_locator)
    blog_detail_page.click_blog_title()
    time.sleep(1)
    blog_detail_page.scroll_to_element(blog_detail_page.sidetab_blog_image_locator)
    blog_image_element = driver.find_element(*blog_detail_page.sidetab_blog_image_locator)
    image_before = blog_image_element.get_attribute("src")
    blog_detail_page.click_sidetab_blog_by_image()
    time.sleep(1)

    opened_image_element = driver.find_element(*blog_detail_page.image_locator)
    image_after = opened_image_element.get_attribute("src")

    assert image_before == image_after, "Blog image is not present or has changed after clicking"