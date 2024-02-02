class a:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    classvariable = "usual classvariable is here"

    def methodA(self):
        print(self.a)

    def whatIsClassVariable(self):
        print(self.classvariable)

b = a(1,2)
b.classvariable = "Not usual class variable"
b.methodA()
b.whatIsClassVariable()

c = a(5,50)
c.methodA()
c.whatIsClassVariable()