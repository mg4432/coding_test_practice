t = int(input()) 

for _ in range(t) : 
    d = {}
    n = int(input()) 
    for i in range(n) : 
        name, cat = input().split()
        if cat not in d : 
            d[cat] = []
        d[cat].append(name)

    if len(d) == 1 : 
        for _ in d : 
            print(len(d[_]))
    else : 
        cnt = 1 
        for nums in d.values() : 
            cnt *= len(nums)+1

        print(cnt-1)
     
    