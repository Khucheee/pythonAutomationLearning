import pytest

@pytest.fixture
def setUp():
    print("launch browser")
    print("login")
    print("Browse products")
    yield
    print("some code after test\n")


def testAddItemToCart(setUp):
    print("item has been added")

def testRemoveItemFromCart(setUp):
    print("Item has been removed")
