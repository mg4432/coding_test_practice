from itertools import product 
n, m = map(int, input().split())
lst = [_ for _ in range(1, n+1)]
answer = []

for c in product(lst, repeat = m) : 
    c = list(c)
    answer.append(c)
    
for ans in answer : 
    for s in ans : 
        print(s, end = ' ')