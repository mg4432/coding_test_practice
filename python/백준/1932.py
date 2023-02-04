n = int(input())

lst = []
for i in range(n) : 
    lst.append(list(map(int, input().split())))

for i in range(1, n) :  
    lst[i][0] += lst[i-1][0]
    lst[i][-1] += lst[i-1][-1]
    
    if i >= 2 :  
        for k in range(1, len(lst[i])-1) : 
            lst[i][k] += max(lst[i-1][k-1], lst[i-1][k])

print(max(lst[-1]))