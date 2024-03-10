def somefunc(b):
    print("somefunc started with argument",b)
    def otherfunc(a):
        return a*10
    return otherfunc

c = somefunc("text")(77)
print(c)