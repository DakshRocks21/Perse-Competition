total, guests = int(input()), int(input())

left = total

while left > total//2 and guests > 0 and left >=2:
    guests -= 1
    left -= 2
while left > 0 and guests > 0:
    guests -= 1
    left -= 1

print(left)