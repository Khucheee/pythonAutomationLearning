def addition(a,b):
    return a+b
print(addition(7,7))

def login(user,password):
    if user=="Alfred" and password=="Khuchashev":
        print("bravo")
        return True
    else:
        return False
if login("Alfred","Khuchashev"):
    print("what a genius logic in this case")