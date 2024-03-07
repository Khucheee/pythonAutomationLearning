import pytest


@pytest.fixture(autouse=True)
def lesson6():
    print("there is some code from conftest file for lesson6")

