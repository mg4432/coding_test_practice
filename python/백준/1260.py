from collections import deque
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) : 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 

graph = [sorted(g) for g in graph]

def dfs(graph, start, visited) : 
    answer = []
    visited[start] = True 
    for i in graph[v] : 
        if not visited[i] : 
            dfs(graph, i, visited)
            answer.append(i)


def bfs(graph, start, visited) : 
    global v
    answer = str(v)
    q = deque([start])
    visited[start] = True 
    while q : 
        v = q.popleft()
        for i in graph[v] : 
            if not visited[i] : 
                q.append(i)
                visited[i] = True
                answer += ' ' + str(i)
    return answer

visited = [False] * (n+1)
bfs_result = bfs(graph, v, visited)




