N, r, c = map(int, input().split())
answer = 0 

if N == 1 : 
    check = (r, c)
    if check == (0, 0) :
        print('0')
    elif check == (0, 1) : 
        print('1')
    elif check == (1, 0) : 
        print('2')
    else : 
        print('3')
else : 
    # 2, 2, 1
    while N >= 1 : 
        rloc1, rloc2 = divmod(r, 2**(N-1)) # 1, 0
        cloc1, cloc2 = divmod(c, 2**(N-1)) # 0, 1

        answer += (2*rloc1 + cloc1) * 2**((N-1)*2)
        r = rloc2
        c = cloc2
        N -= 1

    check = (rloc2, cloc2)
    if check == (0, 0) : 
        answer += 1
    elif check == (0, 1) :
        answer += 2 
    elif check == (1, 0) : 
        answer += 3
    else : 
        answer += 4

    print(answer-1)