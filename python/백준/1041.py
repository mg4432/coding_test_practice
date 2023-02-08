from itertools import combinations 
n = int(input()) 
lst = list(map(int, input().split())) 

if n == 1 : 
    print(sum(sorted(lst)[:-1]))
    
else :
    min_lst = []
    min_lst.append(min(lst[0], lst[5]))
    min_lst.append(min(lst[1], lst[4]))
    min_lst.append(min(lst[2], lst[3]))
    min_lst.sort()

    min1 = min_lst[0]
    min2 = sum(min_lst[:2])
    min3 = sum(min_lst)
     
    answer = 0 
    answer += (4*(n-1)*(n-2) + (n-2)**2) * min1
    answer += 4*(2*n-3) * min2
    answer += 4 * min3
    print(answer)