n = int(input()) 
table = [list(map(int, input().split())) for _ in range(n)]
table.sort(key = lambda x: (x[1], x[0]))

cnt, end = 0, 0
for i in range(n) : 
    if table[i][0] >= end : 
        end = table[i][1]
        cnt += 1 
           
print(cnt)