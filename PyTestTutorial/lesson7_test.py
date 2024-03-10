import pytest


@pytest.fixture(params=["a","b"])
def lesson7(request):
    print("lesson 7 fixture! with",request.param)

def testLes7v1(lesson7):
    print("\nlesson7.1 text")

def testLes7v3(lesson7):
    print("lesson7.3 text")

@pytest.mark.parametrize("a, b, final",[(1,2,3),(2,2,4),(1,4,5)])
def testLes7v2(lesson7,a,b,final):
    print("\n",a,"+",b)
    assert a+b==final
    print("\nlesson7.2 text")


