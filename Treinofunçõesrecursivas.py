

def fatoria(x):
    if x == 1 or x == 0 :
        return 1

    return  x*fatoria(x-1)

print(fatoria(5))
