import pytest

@pytest.mark.odd
def testOne():
    print("first test")

def testTwo():
    print("second test")

@pytest.mark.odd
def testThree():
    print("third test")

def testFour():
    print("fourth test")
@pytest.mark.odd
def testFive():
    print("fiveth test")
