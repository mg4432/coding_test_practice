
def get_lst(lst) : 
    if len(lst) == 2 : 
        lst = deque([])
    else : 
        lst = lst[1:-1].split(',')
        lst = deque([int(x) for x in lst])
    return lst
    
def print_string(lst) : 
    if lst == 'error' : 
        return 'error'
    else : 
        if stat == 1 : 
            lst.reverse()
        s = ','.join([str(x) for x in lst])
        return '[' + s + ']'


def f(cmd, lst) : 
    global stat, cnt
    if cmd == 'R' :
        stat = 1-stat
        cnt += 1 
    
    else : 
        if len(lst) == 0 : 
            return 'error'
        else :
            if stat == 0 : 
                lst.popleft()
            else : 
                lst.pop()
    
    return lst

t = int(input())

for i in range(t) : 
    stat, cnt = 0, 0
    cmd = input()
    n = int(input())
    lst = get_lst(input())
    
    for c in cmd : 
        lst = f(c, lst)
        if lst == 'error' : 
            break
        
    print(print_string(lst))
        