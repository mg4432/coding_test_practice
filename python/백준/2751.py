import sys

T = int(input())
lst = [int(input()) for _ in range(T)]
lst.sort()

for _ in lst : 
    print(_)
