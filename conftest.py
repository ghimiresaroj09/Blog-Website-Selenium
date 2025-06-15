import pytest
from selenium import webdriver

# Add a command-line option to select browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests"
    )

# Provide the browser value to fixtures
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# WebDriver setup fixture
@pytest.fixture()
def driver(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("Invalid browser: Choose 'chrome', 'firefox', or 'edge'")

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    
