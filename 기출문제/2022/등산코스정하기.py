def solution(n, paths, gates, summits):
    conn = [[] for _ in range(n+1)]
    for i, j, w in paths : 
        conn[i].append((j, w))
        conn[j].append((i, w))

    # 다익스트라 알고리즘
    Max = 10000000
    min_dis = [Max for _ in range(n+1)]
    
    
    answer = []
    return answer

n = 6
path = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]	
gates = [1, 3] 
summits = [5]
print(f'answer : {answer}') 