class one:
    prop = "1"
    def __init__(self):
        print("class one created")
    def classOneMethod(self):
        print("I am first class boi")

class two:
    prop = "2"
    def __init__(self):
        print("class two created")
    def classTwoMethod(self):
        print("i am second class boii")

class three(one,two):
    pass
a = three()
print(a.prop)