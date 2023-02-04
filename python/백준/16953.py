a, b = map(int, input().split())

cnt = 0

# B가 A보다 큰 경우 B를 줄여나감
while b > a :
    cnt += 1
    # B의 가장 오른쪽 수가 1인 경우, B가 1이면 안 됨
    if  str(b)[-1] == '1' : 
        b = int(str(b)[:-1])
    
    # B가 짝수인 경우
    elif b % 2 == 0 : 
        b //= 2
        
    # 1. B의 가장 오른쪽 수가 1이 아닌 홀수
    # 2. B가 10보다 작은 홀수
    else : 
        break
    
if a == b : 
    print(cnt+1)
else : 
    print(-1)