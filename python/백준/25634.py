from itertools import combinations 

n = int(input()) 
light = list(map(int, input().split())) 
status = list(map(int, input().split())) 

sum_status = sum(status)
sum_light = sum(light)

if sum_status == 0 :
    print(sum_light) 

elif sum_status == n : 
    print(sum_light - min(light))
    
else :    
    add = 0      
    lst = [l*(-2*s+1) for l, s in zip(light, status)] 
    for i in range(1, n) :
        lst[i] += lst[i-1]

    lst = list(reversed([0] + lst))

    s = -float('inf')

    for i in range(len(lst)-1) :
        compare = lst[i]
        if compare <= s : 
            continue 
        s = compare
        val = compare - min(lst[i+1:]) 
        if val > add : 
            add = val

    add = max(0, add)
    print(sum([l*s for l, s in zip(light, status)] ) + add)

