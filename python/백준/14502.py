from itertools import combinations 
import copy 

n, m = map(int, input().split()) 

lst = [] 

for _ in range(n) : 
    lst.append(list(map(int, input().split())))

def dfs(x, y) :
    if x < 0 or x >= n or y < 0 or y >= m : 
        return False 

    dd = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    if graph[x][y] == 0 : 
        check = 0
        for dx, dy in dd : 
            if x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= m : 
                continue
            if graph[x+dx][y+dy] == 2 : 
                check = 1
        if check == 1 :    
            graph[x][y] = 2
            dfs(x-1, y)  
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y)
        return True 
    return False 

can = [(x, y) for x in range(n) for y in range(m) if lst[x][y] == 0]

answer = 0 

for comb in combinations(can, 3) : 
    graph = copy.deepcopy(lst) 
    for c in comb : 
        graph[c[0]][c[1]] = 1 
    for i in range(n) : 
        for j in range(m) : 
            dfs(i, j)
    cnt = sum([x.count(0) for x in graph])
    if cnt > answer : 
        answer = cnt

print(answer)
 

