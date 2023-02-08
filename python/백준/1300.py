n = int(input()) 
k = int(input()) 

s, e = 1, n**2 
while s <= e : 
    mid = (s+e)//2 

    cnt = 0
    for i in range(1, n+1) :
        cnt += min(mid//i, n)

    if cnt >= k : 
        e = mid-1 
    else : 
        s = mid+1
print(s)