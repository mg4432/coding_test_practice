import re 
import sys 

n = int(input())
p = re.compile('(100+1+|01)+')

for i in range(n) : 
    sign = str(input().strip())
    print(sign)
    if p.fullmatch(sign) :
        print('YES')
    else : 
        print('NO')