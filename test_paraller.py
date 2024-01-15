import pytest
from selenium import webdriver

@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_open_url(browser):
    if browser =="chrome":
        driver = webdriver.Chrome()
    elif browser =="firefox":
        driver = webdriver.Firefox()
    elif browser =="edge":
        driver = webdriver.Edge()
    try:
         driver.get("https://www.baps.org/")

    finally:
        driver.close()