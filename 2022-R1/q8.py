length = int(input())
alts = [int(input()) for i in range(length)]
a = 0
d = 0

for i in range(len(alts))[:-1]:
    if alts[i] < alts[i+1]:
        a += alts[i+1] - alts[i]
    elif alts[i] > alts[i+1]:
        d += alts[i] - alts[i+1]

print(a)
print(d)