total = 0
while True:
    x = int(input())
    if x == -1:
        break
    total += x

print(str(30*(total//60)))
