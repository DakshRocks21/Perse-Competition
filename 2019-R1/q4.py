n1, n2, n3, n4 = [int(input()) for _ in range(4)]

if n2 - n1 == n3 - n2 == n4 - n3:
    print(n2 - n1)
else:
    print("NO")