seats = [0] + [int(input()) for _ in range(20)] + [0]
ans = 0


for i, curr in list(enumerate(seats))[1:-1]:
    if curr == seats[i-1] == seats[i+1] == 0:
        seats[i] = 1
        ans += 1

print(ans)