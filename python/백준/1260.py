from collections import deque  

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) : 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 

graph = [sorted(g) for g in graph]

def dfs(v) : 
    visited_dfs[v] = 1
    print(v, end = ' ')
    for i in graph[v] :
        if visited_dfs[i] == 0 : 
            dfs(i) 

def bfs(v) : 
    q = deque([v])
    visited_bfs[v] = True 
    while q : 
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v] : 
            if not visited_bfs[i] : 
                q.append(i)
                visited_bfs[i] = True

visited_bfs = [False] * (n+1) 
visited_dfs = [False] * (n+1) 

dfs(v)
print()
bfs(v)
