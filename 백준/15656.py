from itertools import product

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []
for p in product(lst, repeat = m) : 
    answer.append(p)
    
for ans in answer : 
    for s in ans : 
        print(s, end = ' ')
