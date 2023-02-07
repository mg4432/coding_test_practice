import math

n = int(input())
lst = sorted([int(input()) for _ in range(n)])
new_lst = [lst[i]-lst[i-1] for i in range(1, len(lst))]

def get_gcd(lst) : 
    val = lst[0]
    for i in range(1, len(lst)) : 
        val = math.gcd(val, lst[i])
    return val

def f(n) :
    ret = [] 
    for i in range(1, int(math.sqrt(n))+1) : 
        if n % i == 0 : 
            ret.append(i)
            ret.append(n//i)
    return sorted(list(set(ret)))

result = f(get_gcd(new_lst))
for x in result : 
    if x != 1 : 
        print(x, end = ' ')