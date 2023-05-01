import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    driver = webdriver.Chrome()
    return driver

   # if browser == 'chrome':
   #     driver = webdriver.Chrome()
   # elif browser == 'firefox':
   #     driver = webdriver.Firefox()
   # else:
   #     driver = webdriver.Edge()
    # return driver


# def pytest_addoption(parser):
#   parser.addoption("--browser")


# @pytest.fixture()
# def browser(request):
#   return request.config.getoption("--browser")


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata["Project Name"] = "Mercury Tours"
