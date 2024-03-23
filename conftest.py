import pytest, yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture(scope="session")
def browser():
    if testdata["browser"] == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions
        driver = webdriver.Chrome(service, options=options)
    else:
        raise NameError("Browser not found.")
    yield driver
    driver.quit()
