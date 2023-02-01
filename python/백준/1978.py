import math 

def check(n) : 
    if n == 1 : 
        return False 
    
    if n == 2 : 
        return True 
    
    for i in range(2, int(math.sqrt(n)) + 1) : 
        if n % i == 0 : 
            return False
    return True

T = int(input())
lst = list(map(int, input().split()))

answer = 0
for n in lst : 
    if check(n) :
        answer += 1 
print(answer)
            