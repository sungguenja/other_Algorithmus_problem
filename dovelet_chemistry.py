X=True
before = None
while X:
    after = float(input())
    if after == 999:
        X=False
    else:
        if before == None:
            before = after
        else:
            print(after-before)
            before = after
print("EoO")