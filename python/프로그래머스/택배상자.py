from collections import deque 

def solution(order) : 
    q = deque([x for x in range(1, len(order) + 1)])
    stack = deque()
    cnt = 0 
    
    while q : 
        if q[0] != order[cnt] : 
            if stack and stack[-1] == order[cnt] : 
                cnt += 1
                stack.pop()
                
            else : 
                stack.append(q.popleft())
                
        else : 
            cnt += 1 
            q.popleft()
        
    while stack : 
        if stack[-1] == order[cnt] : 
            cnt += 1 
            stack.pop()
            
        else : 
            break 
            
    return cnt