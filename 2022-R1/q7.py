x = int(input())

if x%2 == 1:
    print(x)
else:    
    while x%2 != 1:
        x = x//2
    print(x)