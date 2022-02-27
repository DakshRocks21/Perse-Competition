x = input()

for i in range(3):
    if int(x[i+1]) <= int(x[i]):
        print(x[i+1])

