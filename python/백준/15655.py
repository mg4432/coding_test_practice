import sys 
from itertools import combinations 
n, m = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

answer = []
for c in combinations(lst, m):
    answer.append(c)
    
for ans in answer :
    for s in ans : 
        print(s, end = ' ')