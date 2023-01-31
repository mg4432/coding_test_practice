from itertools import combinations_with_replacement
n, m = map(int, input().split())
lst = [i for i in range(1, n+1)] 
answer = [] 

for c in combinations_with_replacement(lst, m) : 
    answer.append(c)
    
answer.sort()

for ans in answer : 
    for s in ans : 
        print(s, end = ' ')