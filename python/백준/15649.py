from itertools import permutations 
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = map(int,input().split())

answer = []
for p in permutations([(i+1) for i in range(n)], m) : 
    answer.append(p)
    
answer.sort()

for lst in answer : 
    for s in lst : 
        print(s, end = ' ')