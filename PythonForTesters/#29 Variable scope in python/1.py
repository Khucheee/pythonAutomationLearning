what="definetely not what"
def sayWhat():
    what="What?"
    print(what)
sayWhat()
print(what)
where ="difinetely not where"
def sayWhere():
    global where
    where="Where?"
    print(where)
    def youAre():
        print(where+" you are")
    youAre()
    
sayWhere()
print(where)