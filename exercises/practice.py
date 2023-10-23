def indexit(word: str,ind: int)-> str:
    if (ind>=len(word)):
        return("Too high of an index!")
    else:
        return word[ind]

print(indexit("hello",0))


