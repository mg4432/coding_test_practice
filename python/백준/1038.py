from itertools import combinations 
n = int(input())

lst = []

for i in range(1, 11) : 
    for c in combinations(range(10), i) : 
        l = sorted(list(c), reverse = True)
        lst.append(int(''.join(map(str, l))))

lst.sort()

try : 
    print(lst[n])
except : 
    print(-1)
