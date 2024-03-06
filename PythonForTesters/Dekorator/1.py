#it is middleware
def decorat(somefunction):
    def inside():
        print("i am func to add something")
        somefunction()
    return inside()

@decorat
def f():
    print("I am just a simple func")
