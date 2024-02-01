a = range(10)
print(max(a))
print(min(a))
i = iter(a)

while True:
    if next(i)==9:
        break

b = [1,2,3,4,5,6,7,8]
c = slice(0,3)
print(b,b[c])

d ="hello"
e = sorted(d)
print(e)
f = input("Input something to wonder me: ")
print("you printed %s, WOOOW"%(f))





