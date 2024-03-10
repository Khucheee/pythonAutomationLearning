class FirstClass:
    def first(self):
        print("this is first class method")

class Second:
    def __init__(self,firstclass):
        self.firstclass = firstclass


one = FirstClass()
two = Second(one)
