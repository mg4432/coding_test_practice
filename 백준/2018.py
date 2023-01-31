T = int(input())
lst = []

for _ in range(T) : 
    lst.append(int(input()))

lst.sort()

def mean(lst) :
    return round(sum(lst) / len(lst))

def median(lst) : 
    length = len(lst)
    if length % 2 == 0 : 
        return (lst[length-1] + lst[length]) / 2
    
    else : 
        return lst[length // 2]

def mode(lst) : 
    val_dict = {}
    for val in lst : 
        if val in val_dict : 
            val_dict[val] += 1 
        else : 
            val_dict[val] = 1
            
    max_ = 0
    max_lst = []
    for key, value in val_dict.items() : 
        if value > max_ :
            max_lst = []
            max_ = value
            max_lst.append(key)
            
        if value == max_  : 
            max_lst.append(key)
    
    max_lst = list(set(max_lst))
    max_lst.sort()
    
    if len(max_lst) <= 1 : 
        return max_lst[0]
        
    else : 
        return max_lst[1]
        
    

def range_(lst) : 
    max_ = max(lst)
    min_ = min(lst)
    return max_ - min_

print(mean(lst))
print(median(lst))
print(mode(lst))
print(range_(lst))