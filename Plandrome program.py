def palandrome(word):
    x1=word[0]
    y1=word[-1]
    if x1==y1:
        return True
    else:
        return False
x=input("Enter a name:")
print(palandrome(x))
    
