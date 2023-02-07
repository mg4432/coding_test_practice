import sys 
n = int(sys.stdin.readline()) 
lst = set()

for _ in range(n) : 
    s = sys.stdin.readline().strip().split()
    if len(s) == 1 : 
        cmd = s[0]
    else :
        cmd, x = s[0], int(s[1]) 

    if cmd == 'add' :
        lst.add(x)

    elif cmd == 'remove' :
        lst.discard(x) 

    elif cmd == 'check' : 
        print(1 if x in lst else 0)

    elif cmd == 'toggle' : 
        if x in lst : 
            lst.discard(x) 
        else : 
            lst.add(x) 

    elif cmd == 'all' : 
        lst = set([i for i in range(1, 21)])

    else : 
        lst = set()