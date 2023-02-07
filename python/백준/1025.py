import math 

n, m = map(int, input().split()) 
lst = [] 
for _ in range(n) : 
    l = list(input()) 
    lst.append(l) 

best = -1 

for i in range(n) : 
    for j in range(m) : 
        for dn in range(-n, n) : 
            for dm in range(-m, m) : 
                if dn == 0 and dm == 0 : 
                    continue 
                r, c = i, j
                num = ''

                while (0 <= r < n) and (0 <= c < m) : 
                    num += lst[r][c]
                    numint = int(num)
                    if math.sqrt(numint) == int(math.sqrt(numint)) : 
                        if numint > best : 
                            best = numint 

                    r += dn 
                    c += dm

print(best)