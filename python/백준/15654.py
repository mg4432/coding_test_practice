import sys 
from itertools import permutations 

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []
for p in permutations(lst, m) : 
    answer.append(p)
    
for ans in answer : 
    for s in ans : 
        print(s, end = ' ')