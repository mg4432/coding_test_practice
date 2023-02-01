l = int(input())
lst = list(map(int, input().split()))
n = int(input())

idx = 0
cnt = 0

lst.append(0)
lst.sort()

if n in lst : 
    print(0)

else : 
    for i in range(len(lst)) : 
        if lst[i] < n and lst[i+1] > n : 
            idx = i
            break
    
    itv = list(range(lst[idx] + 1, lst[idx+1]))
    
    sp = [i for i in itv if i <= n]
    ep = [i for i in itv if i >= n]
    
    print(len(sp) * len(ep) - 1)