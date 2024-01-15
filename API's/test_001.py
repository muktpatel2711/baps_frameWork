import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Quit the WebDriver after the test
    driver.quit()

def test_case_001(driver):
    driver.get("https://example.com")
    assert driver.title == "Expected Title"
