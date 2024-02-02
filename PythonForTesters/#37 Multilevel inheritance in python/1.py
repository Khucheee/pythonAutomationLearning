class first:
    def __init__(self):
        print("first class created")
class second(first):
    pass
class third(second):
    pass

a = third()