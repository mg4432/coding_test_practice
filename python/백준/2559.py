n, k = map(int, input().split())
temp = list(map(int, input().split()))

answer = []
sp = 0
ep = k

tempsum = sum(temp[sp:ep])
answer.append(tempsum)

while True : 
    sp += 1 
    ep += 1 
    
    if ep > n : 
        break
        
    tempsum -= temp[sp-1]
    tempsum += temp[ep-1]
    
    answer.append(tempsum)
    
print(max(answer))
    
    