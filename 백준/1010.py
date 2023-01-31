import math

def combination(n, r) : 
    return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))

T = int(input())

for t in range(T) : 
    n, m = map(int, input().split())
    print(int(combination(m, n)))
    