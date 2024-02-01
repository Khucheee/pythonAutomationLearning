a = [1,2,3,4,5]
b = ["one","two","three","four","five"]
c = zip(a,b)
print(str(c))
print(set(c))
print(tuple(c))
print(dict(c))
for x,y in zip(a,b):
    print(x,":",y)