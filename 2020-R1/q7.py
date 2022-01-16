'''
52-100 = east
51-99 = west
0-50 = north
49-1 = south
'''
num = []
for _ in range(3):
    x = int(input())
    num.append(x)

for i in range(len(num)):
    # EVEN
    if num[i] >= 52 and num[i]%2 == 0:
        print("east")
    elif num[i] <=50 and num[i]%2 == 0:
        print("north")
    # ODD
    elif num[i] >= 51 and num[i]%2 != 0:
        print("west")
    elif num[i] <= 49 and num[i]%2 != 0:
        print("south")
