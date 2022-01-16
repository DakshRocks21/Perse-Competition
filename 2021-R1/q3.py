a, b, c = int(input()), int(input()), int(input())

a2 = a//2
b += a-a2

b2 = b//2
c += b-b2

c2 = c//2
a2 += c-c2

print(a2)