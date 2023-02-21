import heapq 

n, m, r = map(int, input().split()) 
t = [0] + list(map(int, input().split())) 
graph = {(i+1) : {} for i in range(n)}

for _ in range(r) : 
    a, b, l = map(int, input().split()) 
    if b in graph[a] : 
        graph[a][b] += l 
    else : 
        graph[a][b] = l 

    if a in graph[b] : 
        graph[b][a] += l 
    else : 
        graph[b][a] = l 


def dijkstra(graph, start) : 
    distances = {node : float('inf') for node in graph} 
    distances[start] = 0 
    queue = [] 
    heapq.heappush(queue, [distances[start], start])
    
    while queue : 
        current_distance, current_destination = heapq.heappop(queue) 

        if distances[current_destination] < current_distance : 
            continue 

        for new_destination, new_distance in graph[current_destination].items() : 
            distance = current_distance + new_distance 
            if distance < distances[new_destination] : 
                distances[new_destination] = distance 
                heapq.heappush(queue, [distance, new_destination])

    return distances

answer = 0
for i in range(1, n+1) :
    item = 0 
    for key, value in dijkstra(graph, i).items() : 
        if value <= m : 
            item += t[key]
    if item > answer : 
        answer = item

print(answer)