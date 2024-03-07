import pytest


@pytest.fixture(params=["a","b"])
def lesson7(request):
    print("lesson 7 fixture!")
    print(request.param)

def testLes7v1(lesson7):
    print("lesson7.1 text")


@pytest.mark.parametrize("a, b, final",[])
def testLes7v2():
    print("lesson7.2 text")

def testLes7v3():
    print("lesson7.3 text")
