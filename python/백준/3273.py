N, M = map(int, input().split())
knows = input()
if knows == '0' : 
    n_know, n_know_lst = 0, [0]
else : 
    n_know, n_know_lst = int(knows[:1]), list(map(int, knows[1:].split()))

party = {} 

for _ in range(M):
    p = list(map(int, input().split()[1:]))
    party[_] = p

for _ in range(M):
    for key, values in party.items():
        if len(set(values).intersection(set(n_know_lst))) > 0:
            n_know_lst.extend(values)
            n_know_lst = list(set(n_know_lst))

answer = 0 
for key, value in party.items() : 
    if len(set(value).intersection(n_know_lst)) == 0 : 
        answer += 1 

print(answer)