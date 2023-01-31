def solution(n, left, right):
    answer = []
    # (0, 2)
    start_r = left // n 
    start_c = left % n 
    end_r = right // n 
    end_c = right % n 
    
    print(start_r, start_c, end_r, end_c)
    # (1, 2)
    answer_lst = []
    for i in range(end_r - start_r + 1 ) : 
        lst = [x for x in range(1, n+1)]
        lst = [x if x > start_r + i else start_r + i + 1 for x in lst]

        if i == 0 : 
            lst = lst[start_c : ]
            answer_lst.append(lst)
            
        else :
            if i == end_r : 
                lst = lst[:end_c+1]
                answer_lst.append(lst)
                
            else  :
                answer_lst.append(lst)
    answer = sum(answer_lst, [])
    return answer[:right-left+1]
            
            