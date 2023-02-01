from collections import deque 
a, b, c = map(int, input().split())
answer = [] 

# 방문하는 경우의 수 
q = deque() 
q.append((0, 0))

# 방문 여부 배열
visited = [[0 for _ in range(b + 1)] for _ in range(a + 1)]

# 초기에 a, b 모두 비어있기 때문에 visited[0][0] = 1로 초기화
visited[0][0] = 1 

# 물을 부어주는 동작 
def pour(x, y) : 
    if not visited[x][y] : 
        visited[x][y] = 1 # 방문 check
        q.append((x, y)) # 경우의 수 추가
        
# bfs 
def bfs() : 
    while q : 
        x, y = q.popleft()
        z = c - x -  y
        if x == 0 :
            answer.append(z)
            
        # a -> b 
        water = min(x, b - y)
        pour(x - water, y + water)
        
        # b -> a 
        water = min(a - x, y) 
        pour(x + water, y - water)
        
        # a -> c 
        water = min(x, c - z) 
        pour(x - water, y)
        
        # c -> a 
        water = min(a - x, z)
        pour(x + water, y)
        
        # b -> c 
        water = min(y, c - z) 
        pour(x, y - water)
        
        # c -> b 
        water = min(b - y, z)
        pour(x, y + water)        

        
bfs()
answer.sort()
print(q)
print(answer)