#if we want use some code before and after cases in different modules, we can describe it in conftest file
#There is 2 approaches:
#first - push fixtured function into test as a argument (not good)
#second - pytest.fixture(autouse=True) (bettter aproach)

#but also we can specify scope of using fixture from conftest
#@pytest.fixture(scope="session) - fixtured func will runs ones before first test, no more
#session = function - fixtured func will be executed before every test
#also can use "class", "module", "package" - more in documentation

