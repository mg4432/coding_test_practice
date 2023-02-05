n, m = map(int, input().split()) 
target = list(map(int, input().split()))
lst = [x for x in range(1, n+1)]

cnt = 0 
while target :
    t = target.pop(0)
    idx = lst.index(t)
    
    if len(lst) == 1 :  
        break

    if idx == 0 : 
        lst.pop(0)
    
    else : 
        if idx > len(lst)//2 :
            cnt += len(lst[idx:])

        else : 
            cnt += idx
        lst = lst[idx:] + lst[:idx]
        lst.pop(0)

print(cnt)