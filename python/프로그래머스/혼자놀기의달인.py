def find(s1, s2, cards):
    answer = 0
    idx_cards = {(k+1) : v for k, v in enumerate(cards)}
    cards_idx = {v : k for k, v in idx_cards.items()}
    
    g1, g2 = [], []
    cards = [0] + cards
    visited = [0 for _ in range(len(cards))]
    start1, start2 = s1, s2
    
    now_idx = cards_idx[s1]
    now = s1
    
    while True : 
        if visited[now_idx] == 0 : 
            g1.append(now)
            visited[now_idx] = 1 
            now_idx = now 
            now = idx_cards[now_idx]
            
        else : 
            break
    
    now_idx = cards_idx[s2]
    now = s2
    
    if s2 in g1 : 
        return 0
    
    while True : 
        if visited[now_idx] == 0 : 
            g2.append(now)
            visited[now_idx] = 1 
            now_idx = now 
            now = idx_cards[now_idx]
            
        else : 
            break
        
    return len(g1) * len(g2)
    
def solution(cards) : 
    arr = [[0 for _ in range(len(cards) + 1)] for _ in range(len(cards) + 1)]
    
    for i in range(1, len(cards) + 1) : 
        for j in range(1, len(cards) + 1) : 
            arr[i][j] = find(i, j, cards)
            
    max_score = max(map(max, arr))
    return max_score