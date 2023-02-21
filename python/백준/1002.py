import math
n = int(input()) 

def distance(a, b) : 
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

for _ in range(n) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) 
    if x1 == x2 and y1 == y2 : 
        if r1 == r2 : 
            print(-1) 
        else : 
            print(0)
        continue 

    if r1 > r2 : 
        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1

    sum_r = r1 + r2 
    dist = distance((x1, y1), (x2, y2))
    
    if dist > sum_r : 
        print(0) 
    
    elif dist == sum_r : 
        print(1)    
        
    else : 
        det = dist + r1
        if det > r2 : 
            print(2) 
        elif det == r2 :
            print(1) 
        else : 
            print(0)