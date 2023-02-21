n = int(input()) 
lst = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(1, n+1) : 
    lst[i] = int(input()) 

dp[1], dp[2] = lst[1], lst[1] + lst[2] 
for i in range(3, n+1) : 
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])

print(dp[n])