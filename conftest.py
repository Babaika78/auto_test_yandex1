import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser():
    o = Options()
    o.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=o)
    yield driver
    driver.quit()