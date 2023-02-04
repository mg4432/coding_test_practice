import math

n = int(input())

def check(n) :
    sqrt = math.sqrt(n)

    if sqrt.is_integer() : 
        return 1
    
    for i in range(1, int(sqrt)+1) : 
        if math.sqrt(n-i**2).is_integer() :
            return 2
        
    for i in range(1, int(sqrt)+1) : 
        for j in range(1, int(sqrt)+1) : 
            val = n - i**2 - j**2
            if val > 0 : 
                if math.sqrt(val).is_integer() : 
                    return 3
    
    return 4

print(check(n))