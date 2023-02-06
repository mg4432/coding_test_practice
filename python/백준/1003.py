dp = [0 for _ in range(41)]
dp[1] = 1

def f(n) : 
    for i in range(2, 41) : 
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

t = int(input())
for _ in range(t) : 
    n = int(input())
    if n == 0 : 
        print('1 0')
    else : 
        print(f(n-1), f(n))