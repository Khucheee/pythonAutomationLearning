#for grouping test cases we can use pytest.mark decorator, this allows to use marks

#@pytest.mark.{markname}
#testFunc():
#print("there is some code inside")

#than in console type: pytest -m {markname}
#@pytest.mark.skip - decorator to skip markered cases
#@pytest.mark.xfailed - marker for cases expected to be failed (for example functionality is not ready)
# this case will be xpassed in console
