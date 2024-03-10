import pytest


@pytest.fixture(autouse=True)
def lesson6(browser):
    if browser=="chrome":
        print("LAUNCHING CHROME")
    print("there is some code from conftest file for lesson6")


#from lesson 8
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--platform")

@pytest.fixture(autouse=True) #params here should be the same as in setup func
def browser(request):
    return request.config.getoption("--browser")