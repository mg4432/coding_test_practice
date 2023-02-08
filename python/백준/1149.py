n = int(input()) 
lst = []
for _ in range(n) : 
    lst.append(list(map(int, input().split())))

for i in range(1, n) : 
    for j in range(3) : 
        house_i = lst[i-1].copy()
        house_i.remove(house_i[j])
        lst[i][j] += min(house_i)

print(min(lst[-1]))

