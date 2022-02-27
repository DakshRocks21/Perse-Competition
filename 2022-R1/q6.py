from socket import SO_ERROR


jake = 0
sorina = 0

j = input()
s = input()

c = ['rock', 'paper', 'scissors']

if j == s:
    jake += 1
    sorina += 1
elif (c.index(j) == 2 and c.index(s) == 0) or c.index(j) < c.index(s):
    jake += 5
elif (c.index(s) == 2 and c.index(j) == 0) or c.index(s) < c.index(j):
    sorina += 5


if jake == 5 or sorina == 5:
    print(f"{jake}-{sorina}")
else:
    jDice = int(input())
    sDice = int(input())
    if jDice > sDice :
        jake += jDice
    else:
        sorina += sDice
print(f"{jake}-{sorina}")
