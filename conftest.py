import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
                     
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")



@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language_name = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
        browser = webdriver.Chrome(options = options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", language_name)
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()
