import sys 

t = int(input())
lst = list(input().split())
res = [[0 for _ in range(t)] for _ in range(t)]

for i in range(t) : 
    res[i][i] = 1 
    
for i in range(t-1) : 
    if lst[i] == lst[i+1] :
        res[i][i+1] = 1
        
for length in range(t-2) : 
    for i in range(t-2-length) :
        j = i + 2 + length
        if lst[i] == lst[j] and res[i+1][j-1] == 1 :
            res[i][j] = 1
            
k = int(input())
for _ in range(k) :
    m, n = map(int, input().split())
    print(res[m-1][n-1])