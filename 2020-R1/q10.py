strength, stamina = int(input()), int(input())
course = input().split("_")[1:-1]

count = 0

for jump in course:
    if len(jump) > strength:
        break
    count += 1
    if count == stamina:
        break

print(count)

