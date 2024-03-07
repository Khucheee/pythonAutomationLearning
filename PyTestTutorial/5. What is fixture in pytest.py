# if we want run some code before particular tests we can use fixture decorator above code that we need repeat before
# particular tests
# also we should hand over fixtured function as an argument to test
# @pytest.fixture
# def fixturedFunction():
# some code

#def testLogin(fixturedFunction):
#somecode

# if we want to add some code after test as a fixture we can use
# yield_fixture
# "some code after test" (it calls as a tear down method)

# also we can use pytest.yield if we want use only tear down code or separate setup and
