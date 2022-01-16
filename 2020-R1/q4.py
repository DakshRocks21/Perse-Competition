x, y, z = int(input()), int(input()), int(input())
j = x * z
s = 0.5 * y * z
diff = j - s
if diff > 0:
    print("Jen")
    print(diff)
else:
    print("Sid")
    print(-diff)