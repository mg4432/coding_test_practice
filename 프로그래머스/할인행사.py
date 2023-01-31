def solution(want, number, discount):
    answer = 0
    d = {k : v for k, v in zip(want, number)}
    check = {k : 0 for k, v in d.items()}
    
    for i in range(10) : 
        if discount[i] in d : 
            check[discount[i]] += 1 
        else : 
            pass
    
    values = []
    if list(check.values()) == number : 
        answer += 1
        
    pos = 0
    while pos + 10 < len(discount) : 
        if discount[pos] in check : 
            check[discount[pos]] -= 1 
            
        if discount[pos+10] in check : 
            check[discount[pos+10]] += 1
            
        if list(check.values()) == number : 
            answer += 1
        
        pos += 1
            
    return answer