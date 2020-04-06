import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', help="Choose language: ru, es, fr or something else")


@pytest.fixture(scope="function")
def language(request):
    lang = request.config.getoption("language")
    if lang == None:
        raise pytest.UsageError("--language should be ru, es, fr or something else")
    return lang


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()