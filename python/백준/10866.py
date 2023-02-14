from collections import deque 

n = int(input()) 
lst = deque() 

for _ in range(n) :
    s = list(input().split())
    if len(s) == 1 : 
        if s[0] == 'pop_front' : 
            if len(lst) == 0 : 
                print('-1')
            else : 
                print(lst.popleft())

        elif s[0] == 'pop_back' : 
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

        elif s[0] == 'front' : 
            if len(lst) == 0 : 
                print('-1')
            else : 
                print(lst[0])

        elif s[0] == 'back' : 
            if len(lst) == 0 : 
                print('-1')
            else : 
                print(lst[-1])

    else : 
        if s[0] == 'push_front' : 
            lst.appendleft(int(s[1]))

        else : 
            lst.append(int(s[1]))
