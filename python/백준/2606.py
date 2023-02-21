from collections import deque 

n = int(input()) 
m = int(input())

graph = {(i+1): [] for i in range(n)}

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 

queue = deque(graph[1])
visited = [0 for _ in range(n+1)]
visited[1] = 1
while queue : 
    val = queue.popleft() 
    if visited[val] == 1 : 
        continue 
    visited[val] += 1 
    for g in graph[val] : 
        queue.append(g)


print(sum(visited)-1)
