from collections import deque 

n = int(input()) 
lst = deque() 

for _ in range(n) :
    s = list(input().split())
    if len(s) == 1 : 
        if s[0] == 'pop' : 
            if len(lst) == 0 : 
                print('-1')
            else : 
                print(lst.pop())

        elif s[0] == 'size' : 
            print(len(lst))

        elif s[0] == 'empty' : 
            if len(lst) == 0 :
                print('1')
            else : 
                print('0')

        else : 
            if len(lst) > 0 : 
                print(lst[-1])
            else : 
                print('-1')

    else : 
        lst.append(int(s[1]))

