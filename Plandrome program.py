def palandrome(word):
    x1=word[-1::-1]
    if x1==word:
        return True
    else:
        return False
x=input("Enter a name:")
print(palandrome(x))
