class grandpa:
    yo = 77
    def __init__(self):
        print("i am papa class")

    def say(self):
        print("Where is my socks")

class pa(grandpa):
    pass

a = grandpa()
a.say()
print(a.yo)
b = pa()
print(b.yo)
b.say()

