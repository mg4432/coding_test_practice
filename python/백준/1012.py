import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y) : 
    if x <= -1 or x >= nr or y <= -1 or y >= nc :
        return False 

    if graph[x][y] == 1 : 
        graph[x][y] = 0 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y)
        return True 
    return False

t = int(input())

for _ in range(t) : 
    nr, nc, k = map(int, input().split())
    graph = [[0 for _ in range(nc)] for _ in range(nr)]
    for _ in range(k) : 
        r, c = map(int, input().split())
        graph[r][c] = 1

    answer = 0
    for i in range(nr) : 
        for j in range(nc) : 
            if dfs(i, j) == True : 
                answer += 1 

    print(answer)