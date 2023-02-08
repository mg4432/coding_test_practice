def f(n, a, b) :
    if n == 1 : 
        print(a, b) 
    else : 
        f(n-1, a, 6-a-b) 
        print(a, b)
        f(n-1, 6-a-b, b)

n = int(input())
print(2**n-1)
f(n, 1, 3)