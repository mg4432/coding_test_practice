from itertools import product 
from collections import Counter 

n, m = map(int, input().split()) 
lst = list(map(int, input().split())) 
cnt = dict(Counter(lst))
lst = sorted(list(set(lst)))

for p in product(*[lst for _ in range(m)]) : 
    check = 0
    p = list(p)
    subcnt = dict(Counter(p))
    for val in p : 
        if subcnt[val] > cnt[val] : 
            check = 1 
    if check == 0 : 
        print(' '.join([str(x) for x in p]))