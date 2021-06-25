import pytest, subprocess
from selenium import webdriver

driver = None


@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.maximize_window()
    return driver

