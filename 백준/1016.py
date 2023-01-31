n, m = map(int, input().split())
lst = [1 for _ in range(m - n + 1)]
answer = m-n+1

for i in range(2, int(m**0.5 + 1)) :
    squared_num = i ** 2
    min_times = divmod(n-1, squared_num)[0]+1
    for j in range(min_times*squared_num, m+1, squared_num) :
        if lst[j-n] == 1 : 
            lst[j-n] = 0  
            answer -= 1
print(answer)
        