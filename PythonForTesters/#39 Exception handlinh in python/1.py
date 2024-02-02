a = int(input("give me number, please: "))
b = int(input("give me another number, please: "))
if b==7:
    raise Exception("Do not use 7 as the second digit, error bro")
try:
    print("division is: ", a/b)
except Exception as e:
    print("Error has been cathed:",e)
else:
    print("don't worry, there is no any problems")

