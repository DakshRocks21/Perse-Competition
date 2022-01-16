day = int(input())
count = 0

while True:
    fruit = int(input())
    if fruit == -1:
        break
    if fruit >= day:
        count += 1

print(count)