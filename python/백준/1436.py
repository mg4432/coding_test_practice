n = int(input())
cnt = 0
i = 1
while True : 
    if '666' in str(i) :
        cnt += 1
    if cnt == n : 
        break
    i += 1 
print(i)  