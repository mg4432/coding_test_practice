a, b, c = map(int, input().split())
def f(a, b, c) : 
    if b == 1 : 
        return a % c
    else : 
        rec = f(a, b//2, c)
        if b % 2 == 0 : 
            return rec**2%c
        else : 
            return a*rec*rec%c

print(f(a, b, c))