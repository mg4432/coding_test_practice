n = int(input())

dp = [0 for _ in range(n+1)]
dp[1] = 0

i = 1 
while True : 
    if 2**i > n : 
        break 
    dp[2**i] = i 
    i += 1 
i = 1 
while True : 
    if 3**i > n : 
        break 
    dp[3**i] = i 
    i += 1 

for i in range(2, n+1) : 
    if dp[i] == 0 : 
        idx = []
        idx.append(i-1)
        if i%2 == 0 : 
            idx.append(i//2)
        if i%3 == 0 : 
            idx.append(i//3)
        
        val = min([dp[k] for k in idx])
        dp[i] = val + 1

print(dp[-1])