M, N = map(int, input().split())

knows = input()
if len(knows) == 1:
    n_know, p_know = 0, [0]
else:
    n_know, p_know = int(knows[:1]), list(map(int, knows[1:].split()))

party = {}

for _ in range(N):
    p = list(map(int, input().split()[1:]))
    party[_] = p

for _ in range(len(party)):
    for key, values in party.items():
        if len(set(values).intersection(set(p_know))) > 0:
            p_know.extend(values)

p_know = set(p_know)

ans = 0
for key, value in party.items():
    if len(set(value).intersection(p_know)) == 0:
        ans += 1

print(ans)