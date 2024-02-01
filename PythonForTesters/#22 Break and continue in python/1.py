while 1:
    break
    print("it did not breaks")
print("oh, it breaks")
index = 0
while index<10:
    print("before continue",index)
    index+=1
    continue
    print("after continue, there is nothing")
print("watch, continue don't let loop go deeper\nbreak dont'let loop go to the next iteration/code strings inside loop")
while index>0:
    print("Parent loop",index)
    while True and index>9:
        print("we are inside subloop, if use continue/break it will"
              "affect only this loop, not parent")
        if index==10:
            print("index=10, now, use break or we will here forever")
            break
        continue
        print("u will never see this")
    index-=1
else:
    print("Loop finished")
