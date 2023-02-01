import sys 

k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

start = 1
end = max(lst) 

while start <= end :
    mid = (start + end)//2

    t = sum([x // mid for x in lst])
    
    if t >= n : 
        start = mid + 1 
        
    else : 
        end = mid - 1 
        
print(end)