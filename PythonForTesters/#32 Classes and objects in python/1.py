class man:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def sayHelloMyNameIs(self):
        print("No i will not do this. I am %s."%(self.name))

me = man("Alfred",22,89,207)
me.sayHelloMyNameIs()