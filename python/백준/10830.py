n, b = map(int, input().split()) 

def matmul(mat1, mat2) :
    l = len(mat1) 
    res = [[0 for _ in range(l)] for _ in range(l)]
    
    for i in range(l) : 
        for j in range(l) :
            f = mat1[i] 
            b = [m[j] for m in mat2] 
            res[i][j] = sum([x*y for x,y in zip(f, b)])
            
    return res


def f(a, b) :
    if b == 1 : 
        return rem(a) 

    else : 
        rec = f(a, b//2) 
        if b % 2 == 0 : 
            return rem(matmul(rec, rec))
        
        else : 
            return rem(matmul(matmul(rec, rec), a))


def rem(mat) : 
    l = len(mat) 

    for i in range(l) : 
        for j in range(l) : 
            mat[i][j] %= 1000
    return mat

lst = [] 
for _ in range(n) : 
    lst.append(list(map(int, input().split())))

answer = f(lst, b)

for a in (answer) : 
    print(' '.join([str(x) for x in a]))