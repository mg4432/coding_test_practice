n = int(input()) 
lst = list(map(int, input().split()))
lst.sort()
t = int(input())
answer = 0

l, r = 0, n-1
while l < r :
    Sum = lst[l] + lst[r]
    if Sum < t : 
        l += 1 
    elif Sum > t : 
        r -= 1 
    else : 
        answer += 1
        r -= 1
print(answer)


