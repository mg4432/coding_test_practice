from itertools import combinations_with_replacement 

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = [] 
for c in combinations_with_replacement(lst, m) : 
    answer.append(c)
    
for ans in answer : 
    for s in ans : 
        print(s, end = ' ')