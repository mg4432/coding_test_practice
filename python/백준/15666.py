from itertools import product

n, m = map(int, input().split()) 
lst = list(map(int, input().split()))
lst = list(set(lst))

answer = [] 

for p in product(*[lst for _ in range(m)]) : 
    p = list(p)
    if sorted(p) == p and p not in answer: 
        answer.append(p)

answer = sorted(answer)

for l in answer : 
    print(' '.join([str(x) for x in l]))