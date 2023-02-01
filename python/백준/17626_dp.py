import math

n = int(input())
dp = [0, 1]
 
for i in range(2, n+1) : 
    bound = int(math.sqrt(i))+1
    best = min([dp[i-j**2] for j in range(1, bound)])
    dp.append(best+1)
print(dp[-1])

