from itertools import permutations 

n, m = map(int, input().split())
lst = [(i+1) for i in range(n)]
answer = []

for p in permutations(lst, m) : 
    p = sorted(list(p))
    if p not in answer : 
        answer.append(p)
        
for ans in answer : 
    for s in ans : 
        print(s, end = ' ')