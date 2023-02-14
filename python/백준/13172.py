import math 
def f(a, b) : 
    if b == 1 :
        return a % m
    elif b % 2 == 0 :
        tmp = f(a, b//2) 
        return tmp**2 % m
    else : 
        return a * f(a, b-1) % m

n = int(input()) 
m = 1000000007
answer = 0 

for _ in range(n) : 
    x, y = map(int, input().split())
    g = math.gcd(x, y) 
    x, y = x//g, y//g
    answer += y * f(x, m - 2) % m

print(answer%m)